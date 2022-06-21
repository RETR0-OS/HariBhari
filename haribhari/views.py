from django.shortcuts import render
from django.http import HttpResponse
from blogs.models import Blog
#from .models import Writer

# Create your views here.
def home(request):
    try:
        get_blogs = Blog.objects.all()

        posts = Blog.objects.all().order_by("-blog_date")

        first_post = posts[0]
        second_post = posts[1]
        third_post = posts[2]

        data = {
            'first_post': first_post,
            'second_post': second_post,
            'third_post': third_post
        }
    except IndexError:
        data = {}
    return render(request, 'home.html', data)

'''def home(request):
    return render(request, "home.html")'''
