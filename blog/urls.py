from django.urls import path

from . import views

app_name = "blog"

urlpatterns = [
    path("", views.home),
    path("post/<int:id>/", views.post_detail, name="post-detail"),          
]