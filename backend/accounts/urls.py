from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    path('api/login/', views.LoginView.as_view(), name='login'),
    path('api/signup/', views.SignupView.as_view(), name='signup')
]
