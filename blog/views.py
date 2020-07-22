from django.shortcuts import render
from .models import Blog


def all_blogs(request):
    blogs = Blog.objects.order_by('-date') [:4]         #this sorts the blogs by latest date and shows only 4 of 'em.
    return render(request, 'blog/all_blogs.html', {'blogs':blogs})
