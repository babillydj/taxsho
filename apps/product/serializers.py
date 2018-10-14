from rest_framework import serializers

from .models import Product


# serializers
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'name', 'tax_code', 'price')
