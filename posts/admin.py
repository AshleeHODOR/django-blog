from django.contrib import admin
from .models import Post
#reverse = from posts import models


class PostAdmin(admin.ModelAdmin):
    list_display = [
        "title", "subtitle", "author", 
        "status", "created_on"
    ]

admin.site.register(Post, PostAdmin)

