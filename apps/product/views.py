from rest_framework import status, serializers, generics
from rest_framework.permissions import AllowAny
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response

from .models import Product


# serializers
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'name', 'tax_code', 'price')


# views API
class ProductList(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (AllowAny,)


class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (AllowAny,)


@api_view(['GET'])
@permission_classes((AllowAny, ))
def product_list(request):
    products = Product.objects.all()
    price_total = 0
    tax_total = 0
    grand_total = 0
    data = {'list':[]}

    for product in products:
        refundable = 'No'
        if product.refund():
            refundable = 'Yes'
        
        price_total += product.price
        tax_total += product.tax()
        grand_total += product.amount()

        temp = {
            'name': product.name,
            'tax_code': product.tax_code,
            'type': product.type(),
            'refundable': refundable,
            'price': product.price,
            'tax': product.tax(),
            'amount': product.amount()
        }

        data['list'].append(temp)
    
    data['price_subtotal'] = price_total
    data['tax_subtotal'] = tax_total
    data['grand_subtotal'] = grand_total

    return Response(data, status=status.HTTP_200_OK)
