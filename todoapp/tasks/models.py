from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Task(models.Model):
    PRIORITY_CHOICES = [
        ("L","Low"),
        ("M","Medium"),
        ("H","High"),
    ]

    user = models.ForeignKey(User,
                             on_delete=models.CASCADE)
    title = models.CharField(max_length=225)
    description = models.TextField(blank=True)
    due_date=models.DateField(null=True,
                              blank=True)
    created_at = models.DateTimeField(
                 auto_now_add=True)
    completed = models.BooleanField(
                 default=False)
    priority = models.CharField(max_length=1,
                                default="",
                                choices=PRIORITY_CHOICES)
    def __str__(self) -> str:
        return self.title
