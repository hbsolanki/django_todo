from django.urls import path
from .views import todo_complate,todo_delete,todo_add

urlpatterns = [
    path("add/",todo_add,name='todo_add'),
    path("complate/<int:id>/",todo_complate,name='todo_complate'),
    path("delete/<int:id>/",todo_delete,name='todo_delete'),
]
