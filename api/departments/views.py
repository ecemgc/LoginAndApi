from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from rest_framework import filters, status
from rest_framework.response import Response


from common.api_exceptions import BadRequestException, NotFoundException
from common.common_pagination import StandardPagination
from common.order_util import FieldMappedOrdering

from .models import Department
from .serializers import CreateDepartmentSerializer, DepartmentSerializer

class CreateAndListDepartmentView(ListAPIView, APIView, FieldMappedOrdering):
    serializer_class = DepartmentSerializer
    queryset = Department.objects.all()
    filter_backends = [FieldMappedOrdering, filters.SearchFilter]
    ordering_fields_keymap = {
        'name' : 'name' 
    }
    search_fields = ['name', 'id']
    pagination_class = StandardPagination

    def post(self, request, **kwargs):
        serializer = CreateDepartmentSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        try:
            department = Department(**serializer._validated_data)
            department.save()
            return Response({'id': department.id}, status=status.HTTP_201_CREATED)
        except Exception as ex:
            raise BadRequestException("Department not created : {}".format(ex))
        

class DepartmentView(APIView):

    def get(self, request, **kwargs):
        try:
            department = Department.objects.get(id=kwargs['pk'])
            serializer = DepartmentSerializer(department)
            return Response(serializer.data)
        except Department.DoesNotExist:
            raise NotFoundException("Department with id: {} not found".format(kwargs['pk']))
        
    def put(self, request, **kwargs):
        try:
            department = Department.objects.filter(id=kwargs['pk'])

            if not department.exists():
                raise NotFoundException("Department with id: {} not found".format(kwargs['pk']))

            serializer = CreateDepartmentSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            department.update(**serializer.data)
            return Response({"id": kwargs['pk']})    
        except Exception as ex:
            raise BadRequestException(ex)

    def delete(self, request, **kwargs):
        try:
            department = Department.objects.get(id=kwargs['pk'])
            department.delete()
            return Response("Department with id : {} deleted".format(kwargs['pk']), status=status.HTTP_204_NO_CONTENT)
        except Department.DoesNotExist:
            raise NotFoundException("Department with id: {} not found".format(kwargs['pk']))

        