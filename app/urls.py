
from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),                     # главная страница
    path('car/<int:car_id>/', views.detail, name='detail'),  # детальная страница
]

