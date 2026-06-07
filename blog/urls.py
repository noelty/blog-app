from django.urls import path
from .views import PostListView, PostDetailView

from . import views

app_name = "blog"

urlpatterns = [
    path("", PostListView.as_view(), name="home"),
    path("post/<int:id>/", PostDetailView.as_view(), name="post-detail"),          
]