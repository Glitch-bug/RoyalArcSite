from django.shortcuts import render
from .models import BlogPost

def home(request):
    context = {'home': "home"}
    return render(request, "RoyalPages/home.html", context)

def about(request):
    return render(request, "RoyalPages/about.html")

def blog_post(request, title):
    """Display the details of a blog post"""
    post = BlogPost.objects.get(title=title)
    context = {'post': post}
    return render(request, "RoyalPages/post.html", context)

def extractor(array):
    boolean = False
    for item in array:
        item.title = item.title.title()
        item.text = item.text.split()
        item.text = item.text[:100]
        print(len(item.text))
        if len(item.text) == 100:
            boolean = True
        item.text = ' '.join(item.text)
        if boolean:
            item.text+='...'
            boolean = False
    return(array)

def posts(request):
    posts = BlogPost.objects.order_by('date_added')
    posts = extractor(posts)
    context = {'posts': posts}
    return render(request, "RoyalPages/posts.html", context)


def add_posts(request):
    pass