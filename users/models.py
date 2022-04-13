from turtle import title
from django.db import models

# Create your models here.


class User(models.Model):
    user_id = models.IntegerField(null=True, blank=True)
    username = models.TextField(max_length=200, null=True, blank=True)
    avatar_url = models.TextField(
        max_length=200, default='', null=True, blank=True)
    date_created = models.DateTimeField(
        auto_now_add=True, null=True, blank=True)
