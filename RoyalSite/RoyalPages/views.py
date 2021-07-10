import json
import re
from math import floor, ceil

from django.core import serializers
from django.shortcuts import render

from .models import BlogPost, AboutUs, Image

def home(request):
    abouts = AboutUs.objects.all()
    abouts_qs = prep_json(abouts)
    context = {'home':"home", 'abouts': abouts, 'abouts_qs': abouts_qs}
    return render(request, "RoyalPages/home.html", context)

def about(request):
    abouts = AboutUs.objects.all()
    abouts_qs = prep_json(abouts)
    context = {'abouts': abouts, 'abouts_qs': abouts_qs}
    return render(request, "RoyalPages/about.html", context)

def blog_post(request, pk):
    """Display the details of a blog post"""
    post = BlogPost.objects.get(pk=pk)
    post.views = post.views + 1
    post.save()
    context = {'post': post}
    return render(request, "RoyalPages/post.html", context)

def prep_json(query_set):
    case = re.compile('\s')
    briefcase = []
    for item in query_set:
        item.text = item.text.replace('\r', '\\r')
        item.text = item.text.replace('\n', '\\n')
        item.text = item.text.replace("\'", "\\'")
        item.text = item.text.replace('\"', '\\"')
        item.text = item.text.replace('\t', '\\t')
        item.text = item.text.replace('\&', '\\&')
        item.text = item.text.replace('\f', '\\f')
        item.text = item.text.replace('\b', '\\b')
    query_set = serializers.serialize("json", query_set)
    return query_set

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
    posts = BlogPost.objects.order_by('-date_added')
    popular = BlogPost.objects.order_by('views')
    popular = prep_json(popular)
    posts = extractor(posts)
    context = {'posts': posts, 'popular': popular}
    return render(request, "RoyalPages/posts.html", context)

def gallery(request):
    gallery = Image.objects.order_by('-id')
    context = {'gallery': gallery}
    return render(request, "RoyalPages/gallery.html", context)

def add_posts(request):
    pass