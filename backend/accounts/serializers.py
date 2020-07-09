from rest_framework.serializers import ModelSerializer
from django.contrib.auth.models import User 
from .models import userImage
from rest_framework import serializers

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

class userImageSerializer(ModelSerializer):
    # user = UserSerializer(required=False)
    image = serializers.ImageField()
    class Meta:
        model = userImage
        fields = ['id', 'image']
