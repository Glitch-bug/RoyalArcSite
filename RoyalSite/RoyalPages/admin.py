from django.contrib import admin

from .models import BlogPost, AboutUs

admin.site.register(BlogPost)
admin.site.register(AboutUs)