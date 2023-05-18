from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import filters, status

from common.api_exceptions import BadRequestException, NotFoundException
from common.common_pagination import StandardPagination
from common.order_util import FieldMappedOrdering

from .models import Product
from .serializers import CreateProductSerializer, ProductSerializer, UpdateProductSerializer

class CreateAndListProduct(ListAPIView, APIView, FieldMappedOrdering):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    filter_backends = [FieldMappedOrdering, filters.SearchFilter]
    ordering_fields_keymap = {
        'brand' : 'brand',
        'model' : 'model',
        'category' : 'category',
        'department' : 'department' 
    }
    search_fields = ['brand', 'id', 'model', 'category', 'department']
    pagination_class = StandardPagination

    def post(self, request, **kwargs):
        serializer = CreateProductSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        try:
            product = Product.objects.create(**serializer.validated_data)
            return Response({'id' : product.id}, status=status.HTTP_201_CREATED)
        except Exception as ex:
            raise BadRequestException("Product not created : {}".format(ex))


class ProductView(APIView):

    def get(self, request, **kwargs):
        try:
            product = Product.objects.get(id=kwargs['pk'])
            serializer = ProductSerializer(product)
            return Response(serializer.data)
        except Product.DoesNotExist:
            raise NotFoundException("Product with id: {} not found".format(kwargs['pk']))
        
    def put(self, request, **kwargs):
        try:
            product = Product.objects.filter(id=kwargs['pk'])

            if not product.exists():
                raise NotFoundException("Product with id: {} not found".format(kwargs['pk']))

            serializer = UpdateProductSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            product.update(**serializer.data)
            return Response({"id": kwargs['pk']})    
        except Exception as ex:
            raise BadRequestException(ex)

    def delete(self, request, **kwargs):
        try:
            product = Product.objects.get(id=kwargs['pk'])
            product.delete()
            return Response("Product with id : {} deleted".format(kwargs['pk']), status=status.HTTP_204_NO_CONTENT)
        except Product.DoesNotExist:
            raise NotFoundException("Product with id: {} not found".format(kwargs['pk']))
