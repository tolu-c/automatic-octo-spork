from unicodedata import name
from django.urls import path
from . import views

app_name = 'endpoint'

urlpatterns = [
    path('', views.api_overview, name='api_overview'),
    path('eoi-list/', views.eoi_list, name='eoi-list'),
    path('gender-list/', views.gender_list, name='gender-list'),
    path('skill-list/', views.skill_list, name='skill-list'),
    path('education-list/', views.education_list, name='education-list'),
    path('knowledge-list/', views.knowledge_list, name='knowledge-list'),
    path('eoi-detail/<str:pk>/', views.eoi_detail, name='eoi-detail'),
    path('eoi-create/', views.eoi_create, name='eoi-create'),
    path('eoi-update/<str:pk>/', views.eoi_update, name='eoi-update'),
    path('eoi-delete/<str:pk>/', views.eoi_delete, name='eoi-delete'),
    path('user/<str:pk>/', views.getUserById, name='user'),
    path('user-list/', views.userList, name='user-list'),
]
