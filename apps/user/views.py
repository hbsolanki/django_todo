from django.shortcuts import render,redirect
from django.contrib import messages
from django.http import JsonResponse
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login,logout
from .forms import CustomUserCreationForm
from ..todo.models import Todo


def login_view(request):
    if request.user.is_authenticated:
        return redirect("home")
    
    form=AuthenticationForm(request,data=request.POST or None)
    try:
        if form.is_valid():
            login(request,form.get_user())
            return redirect("home")    
    except Exception as e:
        messages.error(request,e)

    return render(request,"login.html",{"form":form})

def register_view(request):
    if request.user.is_authenticated:
        return redirect("home")
    form=CustomUserCreationForm(request.POST or None)
    try:
        if form.is_valid():
            user=form.save()
            login(request,user)
            return redirect("home")
    except Exception as e:
        messages.error(request,e)

    return render(request,"register.html",{"form":form})

def home(request):
    if not request.user.is_authenticated:
        return redirect("user_login")

    todos=Todo.objects.filter(user=request.user)
    return render(request,"home.html",{"todos":todos})

def logout_view(request):
    logout(request)
    return redirect('user_login')
