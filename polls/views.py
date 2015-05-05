from django.http import Http404
from django.shortcuts import get_object_or_404, render

from.models import Todo


def index(request):
    latest_todo_list = Todo.objects.order_by('-deadline_date')
    context = {'latest_todo_list': latest_todo_list}
    return render(request, 'index.html', context)


def detail(request, todo):
    todo = get_object_or_404(Todo, todo_text=todo)
    return render(request, 'detail.html', {'todo': todo})


def impressum(request):
    return render(request, 'impressum.html')


def add(request):
    return render(request, 'add.html')


def edit(request, todo):
    return render(request, 'edit.html')