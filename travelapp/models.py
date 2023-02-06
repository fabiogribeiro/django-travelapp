from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=30)
    body = models.TextField()
    author = models.ForeignKey(User, models.CASCADE, blank=True, null=True)
