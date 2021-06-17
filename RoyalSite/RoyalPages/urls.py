from django.urls import path

from . import views

app_name = "RoyalPages"
urlpatterns = [
    path("", views.home, name="home"),
    path("posts/<str:title>", views.blog_post, name="blog"),
    path("posts", views.posts, name="posts"),
    path("about us", views.about, name="about")
]