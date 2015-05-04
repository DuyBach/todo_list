from django.http import HttpResponse
from django.template import RequestContext, loader
from.models import Todo
from django.shortcuts import render


def index(request):
    latest_todo_list = Todo.objects.order_by('-deadline_date')
    context = {'latest_todo_list': latest_todo_list}
    return render(request, 'polls/index.html', context)


def detail(request, todo_id):
    return HttpResponse("You're looking at question %s." % todo_id)