from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from .models import Todo
from .forms import Todo_forms

from django.utils import timezone
# Create your views here.


def home_view(request):
    item_list = Todo.objects.all()
    todo_object = {
        "object_list": item_list
        }
    return render(request, 'main/index.html', todo_object)


def add_view(request):
    content = request.POST["content"]
    if request.method == "POST":
            Todo.objects.create(text = content)

    return HttpResponseRedirect('/projects/todoapp/')


def delete_view(request, todo_id):
    Todo.objects.get(id=todo_id).delete()
    return HttpResponseRedirect('/projects/todoapp/')

