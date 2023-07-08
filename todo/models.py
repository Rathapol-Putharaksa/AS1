from django.db import models
from django.utils import timezone

def one_week_ago():
    return timezone.now() + timezone.timedelta(days=7)


# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length=80)
    description = models.TextField()
    start_date = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField(default=one_week_ago)
    complete = models.BooleanField(default=False)


    
    def __str__(self):
        return self.title