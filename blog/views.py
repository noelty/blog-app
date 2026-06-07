from typing import Any
from django.urls import reverse
from .models import Post, Comment
from .forms import CommentForm
from django.shortcuts import render, get_object_or_404,redirect
from django.views.generic.list import ListView
from django.views.generic import DetailView
from django.views.generic.edit import FormMixin

class PostListView(ListView):
    model = Post
    context_object_name = "posts"
    template_name = "blog/home.html"

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

class PostDetailView(FormMixin, DetailView):
    model = Post
    form_class = CommentForm
    template_name = "blog/post_detail.html"
    pk_url_kwarg = "id"

    def get_success_url(self):
        return reverse("blog:post-detail", kwargs={"id": self.object.id})

    def form_valid(self, form):
        comment = form.save(commit=False)
        comment.post = self.object
        comment.save()
        return super().form_valid(form)

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        return self.form_invalid(form)
    
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["comments"] = Comment.objects.filter(post=self.object)
        return context




