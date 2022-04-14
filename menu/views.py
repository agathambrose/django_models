from django.http import HttpResponse
from django.shortcuts import render

from menu.models import Menu

# Create your views here.


def create_new_post(request):
  menu = Menu.objects.create(
      title="My post title",
      content="My post body",
      photo_url="https://www.google.com/images/branding/googlelogo/2x/googlelogo_color_272x92dp.png"
  )
  menu.save()
  return HttpResponse("Post successfully created")
