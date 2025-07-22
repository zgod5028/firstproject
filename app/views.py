from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404, redirect
from .models import Car
from .forms import CarForm
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login

def car_list(request):
    cars = Car.objects.all()
    return render(request, 'app/car_list.html', {'cars': cars})

def car_create(request):
    if request.method == 'POST':
        form = CarForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('car_list')
    else:
        form = CarForm()
    return render(request, 'app/car_form.html', {'form': form})

def car_update(request, pk):
    car = get_object_or_404(Car, pk=pk)
    if request.method == 'POST':
        form = CarForm(request.POST, instance=car)
        if form.is_valid():
            form.save()
            return redirect('car_list')
    else:
        form = CarForm(instance=car)
    return render(request, 'app/car_form.html', {'form': form, 'update': True})

def car_delete(request, pk):
    car = get_object_or_404(Car, pk=pk)
    if request.method == 'POST':
        car.delete()
        return redirect('car_list')
    return render(request, 'app/car_confirm_delete.html', {'car': car})

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Регистрация прошла успешно. Войдите в систему.")
            return redirect("login")
        else:
            messages.error(request, "Пожалуйста, исправьте ошибки ниже.")
    else:
        form = UserCreationForm()
    return render(request, "app/register.html", {"form": form})


from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

def login(request):
    if request.method == "POST":
        username = request.POST.get('username', '').strip()
        password = request.POST.get('password', '').strip()

        if not username or not password:
            return render(request, 'login.html', {'error': 'Введите имя пользователя и пароль'})

        user = authenticate(request, username=username, password=password)
        if user:
            auth_login(request, user)
            return redirect('car_list')  # замените на вашу целевую страницу
        else:
            if not User.objects.filter(username=username).exists():
                user = User.objects.create_user(username=username, password=password)
                auth_login(request, user)
                return redirect('car_list')
            else:
                return render(request, 'login.html', {'error': 'Неверный пароль!'})

    return render(request, 'app/login.html')