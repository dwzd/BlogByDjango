from django.shortcuts import render
from blog.models import BlogPosts


# Create your views here.
def blog_index(request):
    blog_list = BlogPosts.objects.all()
    return render(request, 'index.html', {'blog_list': blog_list})
