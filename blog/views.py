from typing import Any
from django.urls import reverse
from .models import Post, Comment
from .forms import CommentForm
from django.views.generic.list import ListView
from django.views.generic import DetailView, CreateView
from django.views.generic.edit import FormMixin
from django.contrib.auth.views import redirect_to_login
from django.contrib.auth.mixins import LoginRequiredMixin

class PostListView(ListView):
    model = Post
    context_object_name = "posts"
    template_name = "blog/home.html"

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
        comment.author = self.request.user
        comment.save()
        return super().form_valid(form)

    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            self.object = self.get_object()
            form = self.get_form()
            if form.is_valid():
                return self.form_valid(form)
            return self.form_invalid(form)
        else:
            return redirect_to_login(request.get_full_path())
    
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["comments"] = Comment.objects.filter(post=self.object)
        return context

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = "blog/post_form.html"
    fields = ["title", "body"]

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)




