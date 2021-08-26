from allauth.account.adapter import get_adapter
from rest_auth.registration.serializers import RegisterSerializer
from rest_framework import serializers
from rest_framework.authtoken.models import Token
from .models import *
from django.contrib.auth.models import User



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'mobile', 'password', 'fullname')


class CustomRegisterSerializer(RegisterSerializer):
    mobile = serializers.CharField(max_length=12)
    fullname = serializers.CharField(max_length=25)

    class Meta:
        model = User
        fields = ('email', 'fullname', 'mobile', 'password')

    def get_cleaned_data(self):
        return {
            'password1': self.validated_data.get('password1', ''),
            'password2': self.validated_data.get('password2', ''),
            'email': self.validated_data.get('email', ''),
            'mobile': self.validated_data.get('mobile', ''),
        }

    def save(self, request):
        adapter = get_adapter()
        user = adapter.new_user(request)
        self.cleaned_data = self.get_cleaned_data()
        user.mobile = self.cleaned_data.get('mobile')
        user.save()
        adapter.save_user(request, user, self)
        return user