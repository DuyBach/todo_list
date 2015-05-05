from datetime import datetime
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Todo(models.Model):
    todo_text = models.CharField('todo', max_length=160)
    todo_perc = models.IntegerField('percentage',
                                    default=0,
                                    validators=[MinValueValidator(0),
                                                MaxValueValidator(100)])
    deadline_date = models.DateField('Deadline Date', default= datetime.now)