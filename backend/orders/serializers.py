from rest_framework import serializers

from .models import Order
from users.serializers import UserProfileSerializer


class OrderSerializer(serializers.ModelSerializer):
    user = UserProfileSerializer(read_only=True)

    class Meta:
        model = Order
        fields = '__all__'

    def validate_total_amount(self, value):
        if value <= 0:
            raise serializers.ValidationError("Total amount must be greater than zero")
        return value

    def validate(self, attrs):
        user = attrs.get('user') or getattr(self.instance, 'user', None) or self.initial_data.get('user')
        if not user:
            raise serializers.ValidationError("User is required to create an order")
        return attrs
