from django.urls import path

from . import views

app_name = "RoyalPages"
urlpatterns = [
    path("", views.home, name="home"),
    path("posts/<int:pk>", views.blog_post, name="blog"),
    path("Posts", views.posts, name="posts"),
    path("About us", views.about, name="about"),
    path("Gallery", views.gallery, name="gallery"),
    path("search", views.search_results, name="search")
]