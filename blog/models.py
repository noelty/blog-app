from django.db import models
from django.utils import timezone

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    created_at = models.DateTimeField(verbose_name="created at", auto_now_add=True)

    def __str__(self) -> str:
        return self.title

class Comment(models.Model):
    name = models.CharField(max_length=50)
    text = models.CharField(max_length=500)
    created_at = models.DateTimeField(verbose_name="created at", auto_now_add=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)