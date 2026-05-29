from rest_framework import permissions, viewsets
from .models import Post
from .serializers import PostSerializer
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

class PostViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """

    queryset = Post.objects.all()
    serializer_class = PostSerializer

def home(request):
    posts = Post.objects.all()

    return render(request, "blog/home.html", {"posts": posts})

def post_detail(request, id):
    post = get_object_or_404(Post, id=id)
    return render(request, "blog/post_detail.html", {"post": post})
