from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_protect

@csrf_protect
def home(request):
    print request.POST

    if request.user.is_authenticated:
        return user_index(request, request.user)

    if 'username' in request.POST and 'password' in request.POST:
        username =request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return user_index(request, user)

    return render(request, 'display/login.html')


def user_index(request, user):
    return render(request, 'display/index.html')

def logout_view(request):
    logout(request)
    return redirect('/')
