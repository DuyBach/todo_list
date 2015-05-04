from django.http import Http404
from django.shortcuts import render

from.models import Todo


def index(request):
    latest_todo_list = Todo.objects.order_by('-deadline_date')
    context = {'latest_todo_list': latest_todo_list}
    return render(request, 'polls/index.html', context)


def detail(request, todo):
    try:
        todo = Todo.objects.get(todo_text=todo)
    except Todo.DoesNotExist:
        raise Http404("Todo does not exist")
    return render(request, 'polls/detail.html', {'Todo': todo})