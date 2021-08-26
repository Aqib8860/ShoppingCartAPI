from rest_framework import serializers
from .models import *
from core.models import *



class CartSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    ordered = serializers.ReadOnlyField()

    class Meta:
        model = Cart
        fields = '__all__'


class UpdateCartSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Cart
        fields = '__all__'
