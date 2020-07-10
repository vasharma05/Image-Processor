from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import *
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
        f = models.CentroidImage()
        f.centroid_0_url = centroid[0]
        f.centroid_1_url = centroid[1]
        f.centroid_2_url = centroid[2]
        f.centroid_3_url = centroid[3]
        f.base_image = user_image
        f.save()
        data = CentroidImageSerializer(f)
        return Response({'detail':'success', 'centroid':data.data}, status=200)

class GradientView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request, format=None):
        id = request.data['id']
        user_image = models.userImage.objects.get(id=request.data['id'])
        image_url = user_image.image.path
        gradient = project.getGradientImage(id, image_url)
        f = models.GradientImage()
        f.gradient_url = gradient[0]
        f.base_image = user_image
        f.save()
        data = GradientImageSerializer(f)
        return Response({'detail':'success', 'gradient':data.data}, status=200)

class NegativeView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request, format=None):
        id = request.data['id']
        user_image = models.userImage.objects.get(id=request.data['id'])
        image_url = user_image.image.path
        negative = project.getNegativeImage(id, image_url)
        f = models.NegativeImage()
        f.negative_url = negative[0]
        f.base_image = user_image
        f.save()
        data = NegativeImageSerializer(f)
        return Response({'detail':'success', 'negative':data.data}, status=200)
    
class NegativeView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request, format=None):
        id = request.data['id']
        user_image = models.userImage.objects.get(id=request.data['id'])
        image_url = user_image.image.path
        negative = project.getNegativeImage(id, image_url)
        f = models.NegativeImage()
        f.negative_url = negative[0]
        f.base_image = user_image
        f.save()
        data = NegativeImageSerializer(f)
        return Response({'detail':'success', 'negative':data.data}, status=200)

class GrayScaleView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request, format=None):
        id = request.data['id']
        user_image = models.userImage.objects.get(id=request.data['id'])
        image_url = user_image.image.path
        grayscale = project.getGrayscaleImage(id, image_url)
        f = models.GrayscaleImage()
        f.grayscale_url = grayscale[0]
        f.base_image = user_image
        f.save()
        data = GrayscaleImageSerializer(f)
        return Response({'detail':'success', 'grayscale':data.data}, status=200)

class SegmentationView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request, format=None):
        id = request.data['id']
        user_image = models.userImage.objects.get(id=request.data['id'])
        image_url = user_image.image.path
        segmentation = project.getSegemtationImage(id, image_url)
        f = models.SegmentationImage()
        f.segmentation_url = segmentation[0]
        f.base_image = user_image
        f.save()
        data = SegmentationImageSerializer(f)
        return Response({'detail':'success', 'segmentation':data.data}, status=200)

class HistogramView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request, format=None):
        id = request.data['id']
        user_image = models.userImage.objects.get(id=request.data['id'])
        image_url = user_image.image.path
        histogram = project.getHistogramEqualization(id, image_url)
        f = models.HistogramImage()
        f.histogram_0_url = histogram[0]
        f.histogram_1_url = histogram[1]
        f.histogram_2_url = histogram[2]
        f.base_image = user_image
        f.save()
        data = HistogramImageSerializer(f)
        return Response({'detail':'success', 'histogram':data.data}, status=200)

class AverageView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request, format=None):
        id = request.data['id']
        user_image = models.userImage.objects.get(id=request.data['id'])
        intensity= request.data['intensity']
        image_url = user_image.image.path
        average = project.getAverageFilter(id, image_url,intensity)
        f = models.AverageImage()
        f.average_url = average[0]
        f.base_image = user_image
        f.save()
        data = AverageImageSerializer(f)
        return Response({'detail':'success', 'average':data.data}, status=200)

class GaussianView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request, format=None):
        print('gaussian')
        id = request.data['id']
        user_image = models.userImage.objects.get(id=request.data['id'])
        image_url = user_image.image.path
        gaussian = project.getGaussionFilter(id, image_url)
        f = models.AverageImage()
        f.gaussian_url = gaussian[0]
        f.base_image = user_image
        f.save()
        data = GaussianImageSerializer(f)
        return Response({'detail':'success', 'gaussian':data.data}, status=200)

class MedianView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request, format=None):
        id = request.data['id']
        user_image = models.userImage.objects.get(id=request.data['id'])
        intensity = request.data['intensity']
        print(intensity)
        image_url = user_image.image.path
        median = project.getMedianFilter(id, image_url,intensity)
        f = models.MedianImage()
        f.median_url = median[0]
        f.base_image = user_image
        f.save()
        data = MedianImageSerializer(f)
        return Response({'detail':'success', 'median':data.data}, status=200)

class SobelView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request, format=None):
        id = request.data['id']
        user_image = models.userImage.objects.get(id=request.data['id'])
        image_url = user_image.image.path
        sobel = project.getSobel(id, image_url)
        f = models.SobelImage()
        f.sobel_url = sobel[0]
        f.base_image = user_image
        f.save()
        data = SobelImageSerializer(f)
        return Response({'detail':'success', 'sobel':data.data}, status=200)

# Return sample data 
# {
#     "detail": "success",
#     "centroid": {
#         "id": 1,
#         "base_image": 9,
#         "centroid_0_url": "http://localhost:8000/media/centroid/centroid_TopLeft_9.png",
#         "centroid_1_url": "http://localhost:8000/media/centroid/centroid_TopRight_9.png",
#         "centroid_2_url": "http://localhost:8000/media/centroid/centroid_BottomLeft_9.png",
#         "centroid_3_url": "http://localhost:8000/media/centroid/centroid_BottomRight_9.png"
#     }
# }