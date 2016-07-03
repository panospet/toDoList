from django.db import models

class Task(models.Model):
    PRIORITIES = (
        ('A', 'Critical'),
        ('B', 'Major'),
        ('C', 'Minor'),
        ('O', 'No priority')
    )

    title = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    priority = models.CharField(max_length=1, choices=PRIORITIES, blank=True)
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title[:20]
