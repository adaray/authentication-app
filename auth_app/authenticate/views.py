from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
#from django.contrib import

# Create your views here.

def home(request):
    return render(request, 'authenticate/home.html',{})

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, ('You are logged in!'))
            return redirect('home')
        else:
            messages.success(request, ('Error logging in!'))
            return redirect('login')
    else:
        return render(request, 'authenticate/login.html',{})

def logout_user(request):
    logout(request)
    messages.success(request, ('You are logged out!'))
    return redirect('home')

def register_user(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form_save()
            username = form.cleaned_data.POST['username']
            password = form.cleaned_data.POST['password1']
            user = authenticate(request, username=username, password=password)
            login(request, user)
            messages.success(request, ('You have registered'))
            return redirect('home')
    else:
        form = UserCreationForm()
        context = {'form': form}
    return render(request, 'authenticate/register.html', context)
