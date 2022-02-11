from django.shortcuts import render
from rest_framework import serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import EoiSerializer
from .models import Eoi


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


@api_view(['GET'])
def eoi_list(request):
    eois = Eoi.objects.all()
    serializer = EoiSerializer(eois, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def eoi_detail(request, pk):
    eoi = Eoi.objects.get(id=pk)
    serializer = EoiSerializer(eoi, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def eoi_create(request):
    serializer = EoiSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['POST'])
def eoi_update(request, pk):
    eoi = Eoi.objects.get(id=pk)
    serializer = EoiSerializer(instance=eoi, data=request.data)

    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['DELETE'])
def eoi_delete(request, pk):
    eoi = Eoi.objects.get(id=pk)
    eoi.delete()

    return Response('Eoi Deleted Successfully')
