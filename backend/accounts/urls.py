from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    path('api/login/', views.LoginView.as_view(), name='login'),
    path('api/signup/', views.SignupView.as_view(), name='signup'),
    path('api/upload/', views.UploadView.as_view(), name = 'upload_view'),
    path('api/images/', views.ImageView.as_view(), name='image'),
    
    path('api/centroid/', views.CentroidView.as_view(), name='centroid'),
    path('api/gradient/', views.GradientView.as_view(), name='gradient'),
    path('api/negative/', views.NegativeView.as_view(), name='negative'),
    path('api/grayscale/', views.GrayScaleView.as_view(), name='grayscale'),
    path('api/segmentation/', views.SegmentationView.as_view(), name='segmentation'),
    path('api/histogram/', views.HistogramView.as_view(), name='histogram'),
    path('api/average/', views.AverageView.as_view(), name='average'),
    path('api/gaussian/', views.GaussianView.as_view(), name='gaussian'),
    path('api/median/', views.MedianView.as_view(), name='median'),
    path('api/sobel/', views.SobelView.as_view(), name='sobel'),

]
