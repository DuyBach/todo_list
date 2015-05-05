from polls.models import Todo

class MovieMixin(object):
    model = Todo
    def get_context_data(self, **kwargs):
        kwargs.update({'object_name':'Todo'})
        return kwargs