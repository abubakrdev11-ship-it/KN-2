from rest_framework import serializers
from .models import Order
from apps.product.models import Product

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['id', 'product', 'quantity', 'total_price', 'created_at']
        read_only_fields = ['total_price', 'buyer']

    def validate(self, data):
        product = data['product']
        if data['quantity'] > product.stock:
            raise serializers.ValidationError("Not enough stock available.")
        return data

    def create(self, validated_data):
        product = validated_data['product']
        validated_data['total_price'] = product.price * validated_data['quantity']
        product.stock -= validated_data['quantity']
        product.save()
        return super().create(validated_data)