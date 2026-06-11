from django.db import models
from django.utils import timezone
from django.conf import settings
from django.urls import reverse
# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    created_at = models.DateTimeField(verbose_name="created at", auto_now_add=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self) -> str:
        return self.title
    def get_absolute_url(self):
        return reverse("blog:post-detail", kwargs={"id": self.id})


class Comment(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)
    text = models.CharField(max_length=500)
    created_at = models.DateTimeField(verbose_name="created at", auto_now_add=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)