from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Task(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=200, null=False)
    description = models.TextField(null=True, blank=True)
    complete = models.BooleanField(default=False)   
    created = models.DateTimeField(auto_now_add=True)

    CATEGORY_CHOICES = [
        ('Work', 'Work'),
        ('Personal', 'Personal'),
        ('Chore', 'Chore'),
    ]

    category = models.CharField(max_length=200, null=False, choices=CATEGORY_CHOICES)
    due_date = models.DateTimeField(null=True,blank=True)

    def __str__(self):
        return self.title
