from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_protect
from django.http import HttpResponseForbidden
from models import CLSniper, Hit


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


def hits(request, sniper_id):
    sniper = CLSniper.objects.get(id=sniper_id)
    if not sniper or not sniper.owner == request.user:
        # TODO: Change this to a different error code?
        return HttpResponseForbidden()
    _hits = Hit.objects.filter(sniper=sniper)
    return render(request, 'display/sniper_details.html', {'sniper': sniper, 'hits': _hits})


