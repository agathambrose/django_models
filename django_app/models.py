from turtle import title
from django.db import models

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=200, null=True, blank=True)
    body = models.TextField(null=True, blank=True)
    photo_url = models.TextField(
        max_length=200, default='', null=True, blank=True)
    date_created = models.DateTimeField(
        auto_now_add=True, null=True, blank=True)


class TestModel(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
