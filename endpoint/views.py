from django.shortcuts import render
from rest_framework import serializers
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework import status
from .serializers import EoiSerializer, SkillSerializer, UserSerializer, UserSerializerWithToken
from .models import Eoi, Skill, Knowledge

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

# Create your views here.


@api_view(['GET'])
def api_overview(request):
    api_urls = {
        'List': '/eoi-list/',
        'Detail': '/eoi-detail/<str:pk>/',
        'Create': '/eoi-create/',
        'Update': '/eoi-update/<str:pk>/',
        'Delete': '/eoi-delete/<str:pk>/',

        'GenderList': '/gender-list',
        'SkillList': '/skill-list',
        'KnowledgeList': '/knowledge-list',
        'EducationList': '/education-list',

        'Userlist': '/user-list',
        'UserDetail': '/user/<str:pk>/'
    }
    return Response(api_urls)


@api_view(['GET'])
# @permission_classes([IsAdminUser])
def userList(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)


@api_view(['GET'])
# @permission_classes([IsAdminUser])
def getUserById(request, pk):
    user = User.objects.get(id=pk)
    serializer = UserSerializer(user, many=False)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getUserProfile(request):
    user = request.user
    serializer = UserSerializer(user, many=False)
    return Response(serializer.data)


@api_view(['GET'])
# @permission_classes([IsAdminUser])
def eoi_list(request):
    eois = Eoi.objects.all()
    serializer = EoiSerializer(eois, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def skill_list(request):
    skills = Skill.objects.all()
    serializer = SkillSerializer(skills, many=True)
    return Response(serializer.data)


@api_view(['GET'])
# @permission_classes([IsAdminUser])
def eoi_detail(request, pk):
    eoi = Eoi.objects.get(id=pk)
    serializer = EoiSerializer(eoi, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def eoi_create(request):
    serializer = EoiSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(status=status.HTTP_200_OK)
    return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
# @permission_classes([IsAdminUser])
def eoi_update(request, pk):
    eoi = Eoi.objects.get(id=pk)
    serializer = EoiSerializer(instance=eoi, data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(status=status.HTTP_200_OK)
    return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
# @permission_classes([IsAdminUser])
def eoi_delete(request, pk):
    eoi = Eoi.objects.get(id=pk)
    eoi.delete()

    return Response('Eoi Deleted Successfully')


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)

        serializer = UserSerializerWithToken(self.user).data
        for k, v in serializer.items():
            data[k] = v

        return data


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer
