from rest_framework import permissions, viewsets
from .models import Post, Comment
from .forms import CommentForm
from .serializers import PostSerializer
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404,redirect

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
    comments = Comment.objects.filter(post=post)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            data = form.save(commit=False)
            data.post = post
            data.save()
            return redirect("blog:post-detail", id=id)
            
    else:
        form = CommentForm()



    return render(request, "blog/post_detail.html", {"post": post, "comments": comments, "form": form})