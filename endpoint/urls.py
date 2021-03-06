from unicodedata import name
from django.urls import path
from . import views
from .views import MyTokenObtainPairView

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

app_name = 'endpoint'

urlpatterns = [
    path('', views.api_overview, name='api_overview'),
    # jwt authentication
    path('login/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # end of jwt authentication
    path('eoi-list/', views.eoi_list, name='eoi-list'),
    path('eoi-detail/<str:pk>/', views.eoi_detail, name='eoi-detail'),
    path('eoi-create/', views.eoi_create, name='eoi-create'),
    path('eoi-update/<str:pk>/', views.eoi_update, name='eoi-update'),
    path('eoi-delete/<str:pk>/', views.eoi_delete, name='eoi-delete'),
    path('user/<str:pk>/', views.getUserById, name='user'),
    path('user-list/', views.userList, name='user-list'),
    path('user-detail/', views.getUserProfile, name='user-detail'),
]
