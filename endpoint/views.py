from django.shortcuts import render
from rest_framework import serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response



# Create your views here.

@api_view(['GET'])
def api_overview(request):
    api_urls = {
        'List': '/eoi-list/',
        'Detail': '/eoi-detail/<str:pk>/',
        'Create': '/eoi-create/',
        'Update': '/eoi-update/<str:pk>/',
        'Delete': '/eoi-delete/<str:pk>/',
    }
    return Response(api_urls)
