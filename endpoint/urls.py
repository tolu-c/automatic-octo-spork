from unicodedata import name
from django.urls import path
from . import views

app_name = 'endpoint'

urlpatterns = [
    path('', views.api_overview, name='api_overview')
]