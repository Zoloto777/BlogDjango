from django.contrib import admin
from .models import Blog, Post, Comment, Blogger

admin.site.register(Blog)
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Blogger)