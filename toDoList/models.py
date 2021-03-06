from django.db import models
from django.contrib.auth.models import User


class Task(models.Model):
    '''
    Module that implements a task for a user. Each task consists of a user,
    a title, a description, a priority, and a flag which indicates if it's
    completed or not.
    '''

    user = models.ForeignKey(User, null=True)
    title = models.CharField(max_length=100, default='<No title>')
    description = models.TextField(max_length=500, default='<No description given>')

    PRIORITIES = (
        ('A', 'Critical'),
        ('B', 'Major'),
        ('C', 'Minor'),
        ('O', 'No priority')
    )
    priority = models.CharField(max_length=1, choices=PRIORITIES, default='O')
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title[:20]
