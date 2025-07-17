from django.shortcuts import render, get_object_or_404
from .models import Car

def index(request):
    cars = Car.objects.all()
    return render(request, 'app/index.html', {'cars': cars})

def detail(request, car_id):
    car = get_object_or_404(Car, id=car_id)
    return render(request, 'app/detail.html', {'car': car})
