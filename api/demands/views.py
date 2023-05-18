from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import filters, status

from common.api_exceptions import BadRequestException, NotFoundException
from common.common_pagination import StandardPagination
from common.order_util import FieldMappedOrdering

from .models import Demand
from .serializers import DemandSerializer, CreateDemandSerializer, UpdateDemandSerializer

class CreateAndListDemandView(ListAPIView, APIView, FieldMappedOrdering):
    serializer_class = DemandSerializer
    queryset = Demand.objects.all()
    filter_backends = [FieldMappedOrdering, filters.SearchFilter]
    ordering_fields_keymap = {
        'sender_employee' : 'sender_employee',
        'department' : 'department',
        'approval_status' : 'approval_status'
    }
    search_fields = ['sender_employee', 'id', 'department']
    pagination_class = StandardPagination

    def post(self, request, **kwargs):
        serializer = CreateDemandSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        try:
            demand = Demand.objects.create(**serializer.validated_data)
            return Response({'id': demand.id}, status=status.HTTP_201_CREATED)
        except Exception as ex:
            raise BadRequestException("Demand not created : {}".format(ex))
        
class DemandView(APIView):

    def get(self, request, **kwargs):
        try:
            demand = Demand.objects.get(id=kwargs['pk'])
            serializer = UpdateDemandSerializer(demand)
            return Response(serializer.data)
        except Demand.DoesNotExist:
            raise NotFoundException("Demand with id: {} not found".format(kwargs['pk']))
        
    def put(self, request, **kwargs):
        try:
            demand = Demand.objects.filter(id=kwargs['pk'])

            if not demand.exists():
                raise NotFoundException("Demand with id: {} not found".format(kwargs['pk']))

            serializer = UpdateDemandSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            demand.update(**serializer.data)
            return Response({"id": kwargs['pk']})    
        except Exception as ex:
            raise BadRequestException(ex)

    def delete(self, request, **kwargs):
        try:
            demand = Demand.objects.get(id=kwargs['pk'])
            demand.delete()
            return Response("Demand with id : {} deleted".format(kwargs['pk']), status=status.HTTP_204_NO_CONTENT)
        except Demand.DoesNotExist:
            raise NotFoundException("Demand with id: {} not found".format(kwargs['pk']))



        
