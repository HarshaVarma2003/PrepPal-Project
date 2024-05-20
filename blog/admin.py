from django.contrib import admin
from .models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'subject', 'date_posted', 'author')
    fields = ('title', 'subject', 'content', 'date_posted', 'author', 'image_url')
admin.site.register(Post, PostAdmin)
