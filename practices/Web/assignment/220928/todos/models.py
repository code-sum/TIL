from email.policy import default
from django.db import models

# Create your models here.


class Todo(models.Model):
    priority = models.CharField(max_length=5)
    content = models.CharField(max_length=80)
    created_at = models.DateField(auto_now_add=True)
    deadline = models.DateField(null=True)
    completed = models.BooleanField(default=False)
