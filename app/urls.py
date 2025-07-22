from django.urls import path
from . import views
from .views import register

urlpatterns = [
    path('car_list/', views.car_list, name='car_list'),
    path('create/', views.car_create, name='car_create'),
    path('update/<int:pk>/', views.car_update, name='car_update'),
    path('delete/<int:pk>/', views.car_delete, name='car_delete'),
    path('register/', register, name='register'),
    path('login/', views.login, name='login'),
]


