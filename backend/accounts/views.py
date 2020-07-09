from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import UserSerializer, userImageSerializer
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from . import models
from image_processing import project 
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
    
class UploadView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request, format=None):
        try:
            data = dict({
                'user': request.user,
                'image': request.data['image']
            })
            serialized_data = userImageSerializer(data = request.data, context={'request':request})
            if(serialized_data.is_valid()):
                serialized_data.save(user = request.user)
            else:
                message = {
                    'detail':serialized_data.errors
                }
                return Response(message, status = 200)
            return Response({'detail':'success', 'response': serialized_data.data}, status=200)
        except:
            return Response({'detail': 'Something went wrong'}, status=500)

class CentroidView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request, format=None):
        id = request.data['id']
        user_image = models.userImage.objects.get(id=request.data['id'])
        image_url = user_image.image.path
        centroid = project.getCentroidImage(id, image_url)
        return Response({'detail':'success'}, status=200)

