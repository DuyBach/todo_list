from django.views.generic import ListView, DeleteView, UpdateView
from polls.models import Todo
from django.views import generic
from polls.forms import TodoName
from django.core.urlresolvers import reverse_lazy


# Create your views here.
class IndexView(generic.ListView):
    template_name = 'index.html'
    context_object_name = 'latest_todo_list'

    def get_queryset(self):
        return Todo.objects.order_by('-deadline_date')


class ImpressumView(generic.ListView):
    template_name = 'impressum.html'
    model = Todo


class AddView(generic.CreateView):
    template_name = 'add.html'
    model = Todo
    success_url = '/'
    fields = ['todo_text', 'deadline_date', 'todo_perc']


class UpdateView(generic.UpdateView):
    template_name = 'edit.html'
    model = Todo
    success_url = '/'
    fields = ['todo_text', 'deadline_date', 'todo_perc']


class DeleteView(TodoName, DeleteView):
    template_name = 'delete_comfirm.html'
    success_url = reverse_lazy('index')