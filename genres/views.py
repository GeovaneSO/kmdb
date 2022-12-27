from django.shortcuts import render
from rest_framework.pagination import PageNumberPagination
from rest_framework.views import APIView, Request, Response, status
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAdminUser

from .models import User
from .serializers import UserSerializer
from rest_framework.generics import ListCreateAPIView
# Create your views here.

class MovieView(ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
