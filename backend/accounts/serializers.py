from rest_framework.serializers import ModelSerializer
from django.contrib.auth.models import User 
from . import models
from rest_framework import serializers



class userImageSerializer(ModelSerializer):
    image = serializers.ImageField()
    class Meta:
        model = models.userImage
        fields = ['id', 'image']

class CentroidImageSerializer(ModelSerializer):
    base_image = serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model = models.CentroidImage
        fields = '__all__'
    
class GradientImageSerializer(ModelSerializer):
    base_image = serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model = models.GradientImage
        fields = '__all__'
class NegativeImageSerializer(ModelSerializer):
    base_image = serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model = models.NegativeImage
        fields = '__all__'

class GrayscaleImageSerializer(ModelSerializer):
    base_image = serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model = models.GrayscaleImage
        fields = '__all__'

class SegmentationImageSerializer(ModelSerializer):
    base_image = serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model = models.SegmentationImage
        fields = '__all__'

class HistogramImageSerializer(ModelSerializer):
    base_image = serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model = models.HistogramImage
        fields = '__all__'

class AverageImageSerializer(ModelSerializer):
    base_image = serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model = models.AverageImage
        fields = '__all__'

class GaussianImageSerializer(ModelSerializer):
    base_image = serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model = models.GaussianImage
        fields = '__all__'

class MedianImageSerializer(ModelSerializer):
    base_image = serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model = models.MedianImage
        fields = '__all__'

class SobelImageSerializer(ModelSerializer):
    base_image = serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model = models.SobelImage
        fields = '__all__'

class UserSerializer(ModelSerializer):
    images = userImageSerializer(read_only=True, many=True)
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password', 'images']
        extra_kwargs = {'password': {'write_only': True}}