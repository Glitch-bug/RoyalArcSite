from django.contrib import admin

from .models import BlogPost, AboutUs, Image

admin.site.register(BlogPost)
admin.site.register(AboutUs)
admin.site.register(Image)