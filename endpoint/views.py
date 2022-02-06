from django.shortcuts import render
from rest_framework import serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response



# Create your views here.

@api_view(['GET'])
def api_overview(request):
    api_urls = {
        'List': '/info-list/',
        'Detail': '/info-detail/<str:pk>/',
        'Create': '/info-create/',
        'Update': '/info-update/<str:pk>/',
        'Delete': '/info-delete/<str:pk>/',
    }
    return Response(api_urls)
