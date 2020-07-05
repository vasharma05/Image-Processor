from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import UserSerializer
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

# Create your views here.

class SignupView(APIView):
    def post(self, request, format=None):
        user = UserSerializer(data = request.data)
        if user.is_valid():
            user.save()
            message = dict()
            user = User.objects.get(username = request.data['username'])
            message['token'] = Token.objects.create(user=user).key
            message['userDetails'] = UserSerializer(user).data
            message['detail'] = 'success'
            return Response(message, status=201)
        else:
            return Response({'error':'Username already exists'}, status=203)

class LoginView(APIView):
    def post(self, request, format=None):
        user = authenticate(username=request.data['username'], password=request.data['password'])
        if user is not None:
            message = dict()
            message['token'] = Token.objects.get_or_create(user = user)[0].key
            serialized_data = UserSerializer(User.objects.get(username=request.data['username']))
            message['userDetails'] = serialized_data.data
            return Response(message, status=200)
        else:
            return Response({'error': 'username or password is incorrect'}, status=200)