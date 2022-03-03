from django.shortcuts import render

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

# def prep_json_popular(query_set):
#     briefcase = []
#     dots = re.compile(r'\\.')
#     for item in query_set:
#         item.title = re.escape(item.title)
#         item.title = item.title.replace('\ ', ' ')
#         item.title = dots.sub('.', item.title)
#         item.title = item.title.replace('.\\', '.')
#         item.text = re.escape(item.text)
#         item.text = item.text.replace('\ ', ' ')
#         item.text =  dots.sub('.', item.text)
#         item.text = item.text.replace('.\\', '.')
        
#         # print(type(item.cover))
#         item.cover = re.escape(str(item.cover))
#         item.cover = item.cover.replace('\ ', ' ')
#         item.cover =  dots.sub('.', item.cover)
#         item.cover = item.cover.replace('.\\', '.')

#     query_set = serializers.serialize("json", query_set)
    # return query_set

def extractor(array, num):
    for item in array:
        if len(item.text.split()) > 10 * num:
            item.title = item.title.title()
            item.text = item.text.split()
            item.text = item.text[:10 * num]
            item.text = ' '.join(item.text)
            item.text+='...'  
    return(array)

def p_extractor(array, num):
    array = list(array)
    for ar in range(len(array)):
        array[ar] = list(array[ar])
    for item in array:
        if len(item[1].split()) > 10 * num:
            item[0] = item[0]
            item[1] = item[1]
            item[1] = item[1].split()
            item[1] = item[1][:10*num]
            item[1] = ' '.join(item[1])
            item[1] += '...'
    return(array)

def diction(alist):
    print(alist)
    diction = {}
    for item in range(len(alist)):
        diction.setdefault(f'item', {'title': alist[item][0], 'text': alist[item][1], 'pk': alist[item][2]})
    print(type(diction))
    return diction

def posts(request):
    posts = BlogPost.objects.order_by('-date_added')
    popular = BlogPost.objects.order_by('-views')
    popular_qs = BlogPost.objects.order_by('-views').values_list('title', 'text', 'pk')
    popular_qs = p_extractor(popular_qs, 2)
    popular = extractor(popular, 2)
    posts = extractor(posts, 10)
    popular_qs = json.dumps(diction(popular_qs))
    # popular_qs = serializers.serialize('json', popular_qs)
    context = {'posts': posts, 'popular': popular, 'popular_qs': popular_qs}
    print(popular_qs)
    return render(request, "RoyalPages/posts.html", context)

def gallery(request):
    gallery = Image.objects.order_by('-id')
    gallery_qs = serializers.serialize("json", gallery)
    context = {'gallery': gallery, "gallery_qs": gallery_qs}
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
            res = 'No matching posts found...'
        return JsonResponse({'data': res})
    return JsonResponse({})

def add_posts(request):
    pass
