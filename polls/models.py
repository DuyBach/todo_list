from django.db import models

class todo(models.Model):
    todo_text = models.CharField('todo', max_length=200)
    todo_perc = models.IntegerField('perc', default=0, max_length=100)
    deadline_date = models.DateTimeField('deadline')