from pyexpat import model
from django.db import models
from django.db.models import fields
from rest_framework import serializers
from .models import Eoi


class EoiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Eoi
        fields = '__all__'
