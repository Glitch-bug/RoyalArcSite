from django.shortcuts import render
from .models import BlogPost

def home(request):
    return render(request, "RoyalPages/home.html")

def about(request):
    return render(request, "RoyalPages/about.html")

def blog_post(request, title):
    """Display the details of a blog post"""
    post = BlogPost.objects.get(title=title)
    context = {'post': post,}
    return render(request, "RoyalPages/post.html", context)

def posts(request):
    posts = BlogPost.objects.order_by('date_added')
    context = {'posts': posts}
    return render(request, "RoyalPages/posts.html", context)