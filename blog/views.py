from django.shortcuts import render, get_object_or_404
from .models import BlogsContent


def all_blogs(request):

    blogs = BlogsContent.objects.order_by('-blogs_date')[:5]
    return render(request, 'blog/all_blogs.html', {'blogs': blogs})


def detail(request, blog_id):
    blog = get_object_or_404(BlogsContent, pk = blog_id)
    return render(request, 'blog/detail.html', {'blog': blog})


