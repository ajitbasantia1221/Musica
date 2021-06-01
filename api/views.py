from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .util import sample
import os

# Create your views here.
# def index(request):
#     return HttpResponse('hello world')
class GenerateMusic(APIView):
    def get(self, request, format=None):
        result = sample(100 , '' , 2048)
        return Response({'message': result}, status= status.HTTP_200_OK)
