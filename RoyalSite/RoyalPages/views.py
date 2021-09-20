import json
import os
import re
from math import floor, ceil

from django.http import JsonResponse
from django.core import serializers
from django.shortcuts import render

from .models import BlogPost, AboutUs, Image

def home(request):
    abouts = AboutUs.objects.all()
    abouts = filename(abouts)
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
    print(post)
    return render(request, "RoyalPages/post.html", context)

def filename(query_set):
    for item in query_set:
        print(item.background)
        item.background = os.path.basename(str(item.background))
    return query_set

def prep_json(query_set):
    case = re.compile(r'\s')
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

def prep_jsons(query_set):
    briefcase = []
    dots = re.compile(r'\\.')
    for item in query_set:
        item.title = re.escape(item.title)
        item.title = item.title.replace('\ ', ' ')
        item.title = dots.sub('.', item.title)
        item.title = item.title.replace('.\\', '.')
        item.text = re.escape(item.text)
        item.text = item.text.replace('\ ', ' ')
        item.text =  dots.sub('.', item.text)
        item.text = item.text.replace('.\\', '.')
    query_set = serializers.serialize("json", query_set)
    return query_set

def extractor(array, num):
    boolean = False
    for item in array:
        item.title = item.title.title()
        item.text = item.text.split()
        item.text = item.text[:10 * num]
        if len(item.text) == 10 * num:
            boolean = True
        item.text = ' '.join(item.text)
        if boolean:
            item.text+='...'
            boolean = False
    return(array)

def posts(request):
    posts = BlogPost.objects.order_by('-date_added')
    popular = BlogPost.objects.order_by('-views')
    popular = extractor(popular, 2)
    posts = extractor(posts, 10)
    popular_qs = prep_jsons(popular)
    context = {'posts': posts, 'popular': popular, 'popular_qs': popular_qs}
    print(popular_qs)
    return render(request, "RoyalPages/posts.html", context)

def gallery(request):
    gallery = Image.objects.order_by('-id')
    gallery_qs = serializers.serialize("json", gallery)
    context = {'gallery': gallery, "gallery_qs": gallery_qs}
    for item in list(gallery):
        print(item)
    return render(request, "RoyalPages/gallery.html", context)

def search_results(request):
    if request.is_ajax():
        post = request.POST.get('post')
        qs = extractor(BlogPost.objects.filter(title__icontains=post), 2)
        if len(qs) > 0 and len(post) > 0:
            data = []
            for pos in qs:
                item = {
                    'pk': pos.pk,
                    'title': pos.title,
                    'text': pos.text,
                    # 'cover': str(pos.cover.url),
                    'date_added': pos.date_added,
                    'views': pos.views
                }
                data.append(item)
            res = data
        else:
            res = 'No posts found...'
        return JsonResponse({'data': res})
    return JsonResponse({})

def add_posts(request):
    pass