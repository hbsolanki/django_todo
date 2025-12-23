from django.shortcuts import render,redirect
from django.contrib import messages
from .models import Todo
from datetime import datetime



def todo_add(request):
    if request.method=="POST":
        try: 
            title=request.POST.get("title")
            todo=Todo(title=title,user=request.user)
            todo.save()
            messages.success(request,"todo added")
        except Exception as e:
            messages.error(request,e)
    
    return redirect("home")


def todo_complate(request,id):
    try:
        todo=Todo.objects.get(id=id)
        todo.complate=True
        todo.complate_at=datetime.now()
        todo.save()
        messages.success(request,f"{todo.title} complate")
    except Exception as e:
        messages.error(request,e)
    return redirect('home')

def todo_delete(request,id):
    try:
        todo=Todo.objects.filter(id=id).delete()
        messages.success(request,f"{todo.title} deleted")
    except Exception as e:
        messages.success(request,e)

    return redirect('home')