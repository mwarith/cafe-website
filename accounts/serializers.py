from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    customer_segment = serializers.ReadOnlyField()

    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'phone_number', 'points_balance', 'total_spent', 'visits_count', 'customer_segment']
        extra_kwargs = {'password': {'write_only': True}}