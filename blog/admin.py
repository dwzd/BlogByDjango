from django.contrib import admin
from blog.models import BlogPosts

# Register your models here.
class BlogPostsAdmin(admin.ModelAdmin):
    list_display = ['title', 'body', 'timestamp']

admin.site.register(BlogPosts, BlogPostsAdmin)
