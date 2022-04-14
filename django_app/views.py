from turtle import title
from django.http import HttpResponse
from django.shortcuts import render

from django_app.models import Post, TestModel

# Create your views here.


def index(request):
    tests = TestModel.objects.all()
    return render(request, 'index.html', {'tests': tests})


def create_post(request, post):
    test = TestModel.objects.create(
        name=post
    )
    test.save()
    return HttpResponse("Post successfully created")

def show_posts(request):
    posts = Post.objects.all()
    return render(request, 'posts_list.html', {'post_list': posts})

def delete_post(request, post):
    test = TestModel.objects.get(name=post)
    test.delete()
    return HttpResponse("Post successfully deleted")

def create_new_post(request):
  post = Post.objects.create(
    title = "My post title",
    body = "My post body",
    photo_url = "https://www.google.com/images/branding/googlelogo/2x/googlelogo_color_272x92dp.png"
  )
  post.save()
  return HttpResponse("Post successfully created")