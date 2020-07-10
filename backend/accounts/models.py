from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class userImage(models.Model):
    user = models.ForeignKey(User, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(default='', upload_to='images/')


class CentroidImage(models.Model):
    base_image = models.ForeignKey(userImage, related_name='centroid', on_delete = models.CASCADE)
    centroid_0_url = models.CharField(max_length=256, default='')
    centroid_1_url = models.CharField(max_length=256, default='')
    centroid_2_url = models.CharField(max_length=256, default='')
    centroid_3_url = models.CharField(max_length=256, default='')

class GradientImage(models.Model):
    base_image = models.ForeignKey(userImage, related_name='gradient', on_delete = models.CASCADE)
    gradient_url = models.CharField(max_length=256, default='')
        
class NegativeImage(models.Model):
    base_image = models.ForeignKey(userImage, related_name='negative', on_delete = models.CASCADE)
    negative_url = models.CharField(max_length=256, default='')

class GrayscaleImage(models.Model):
    base_image = models.ForeignKey(userImage, related_name='grayscale', on_delete = models.CASCADE)
    grayscale_url = models.CharField(max_length=256, default='')

class SegmentationImage(models.Model):
    base_image = models.ForeignKey(userImage, related_name='segmentation', on_delete = models.CASCADE)
    segmentation_url = models.CharField(max_length=256, default='')

class HistogramImage(models.Model):
    base_image = models.ForeignKey(userImage, related_name='histogram', on_delete = models.CASCADE)
    histogram_0_url = models.CharField(max_length=256, default='')
    histogram_1_url = models.CharField(max_length=256, default='')
    histogram_2_url = models.CharField(max_length=256, default='')

class AverageImage(models.Model):
    base_image = models.ForeignKey(userImage, related_name='average', on_delete = models.CASCADE)
    average_url = models.CharField(max_length=256, default='')

class GaussianImage(models.Model):
    base_image = models.ForeignKey(userImage, related_name='gaussian', on_delete = models.CASCADE)
    gaussian_url = models.CharField(max_length=256, default='')

class MedianImage(models.Model):
    base_image = models.ForeignKey(userImage, related_name='median', on_delete = models.CASCADE)
    median_url = models.CharField(max_length=256, default='')

class SobelImage(models.Model):
    base_image = models.ForeignKey(userImage, related_name='sobel', on_delete = models.CASCADE)
    sobel_url = models.CharField(max_length=256, default='')