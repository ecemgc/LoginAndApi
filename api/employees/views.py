from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import filters, status
from common.api_exceptions import BadRequestException, NotFoundException
from common.common_pagination import StandardPagination

from common.order_util import FieldMappedOrdering

from .models import Employee
from .serializers import EmployeeSerializer, CreateEmployeeSerializer, LoginSerializer

from rest_framework.exceptions import AuthenticationFailed
from rest_framework.permissions import AllowAny
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated, AllowAny



class CreateAndListEmployeeView(ListAPIView, APIView, FieldMappedOrdering):

    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all()
    filter_backends = [FieldMappedOrdering, filters.SearchFilter]
    ordering_fields_keymap = {
        'first_name' : 'first_name' 
    }
    search_fields = ['first_name', 'id']
    # pagination_class = StandardPagination


    def post(self, request, **kwargs):
        serializer = CreateEmployeeSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        department_id = serializer.validated_data.pop('department')
        password = serializer.validated_data.pop('password')

        try:
            employee = Employee(**serializer.validated_data)
            employee.set_password(password)
            employee.department_id = department_id
            employee.save()
            return Response({'id': employee.id}, status=status.HTTP_201_CREATED)
        except Exception as ex:
            raise BadRequestException("Employee not created : {}".format(ex))
        

class EmployeeView(APIView):

    def get(self, request, **kwargs):
        try:
            employee = Employee.objects.get(id=kwargs['pk'])
            serializer = EmployeeSerializer(employee)
            return Response(serializer.data)
        except Employee.DoesNotExist:
            raise NotFoundException("Employee with id: {} not found".format(kwargs['pk']))
        
    def put(self, request, **kwargs):
        try:
            employee = Employee.objects.filter(id=kwargs['pk'])

            if not employee.exists():
                raise NotFoundException("Employee with id: {} not found".format(kwargs['pk']))

            serializer = CreateEmployeeSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            employee.update(**serializer.data)
            return Response({"id": kwargs['pk']})    
        except Exception as ex:
            raise BadRequestException(ex)

    def delete(self, request, **kwargs):
        try:
            employee = Employee.objects.get(id=kwargs['pk'])
            employee.delete()
            return Response("Employee with id : {} deleted".format(kwargs['pk']), status=status.HTTP_204_NO_CONTENT)
        except Employee.DoesNotExist:
            raise NotFoundException("Employee with id: {} not found".format(kwargs['pk']))
        


class LoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        employee = authenticate(username=serializer.validated_data['username'], password=serializer.validated_data['password'])

        if employee is not None:
            return Response(get_employee_response(employee))
        else:
            raise AuthenticationFailed()


def get_employee_response(employee):
    refresh = RefreshToken.for_user(employee)
    return {
            'first_name': employee.first_name,
            'last_name': employee.last_name,
            'email': employee.email,
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }


    


