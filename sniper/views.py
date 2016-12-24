from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_protect

from models import CLSniper

@csrf_protect
def home(request):
    if request.user.is_authenticated:
        return user_index(request, request.user)

    return render(request, 'display/login.html')


def user_index(request, user):
    snipers = CLSniper.objects.filter(owner=user)
    return render(request, 'display/index.html', {'snipers':snipers})

def login_view(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        login(request, user)
    return redirect('/')

def logout_view(request):
    logout(request)
    return redirect('/')
