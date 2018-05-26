# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    user_level = models.BooleanField(max_length=5)
    description = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Post(models.Model):
    post = models.CharField(max_length=100)
    user = models.ForeignKey(User,related_name="post_creator")
    reciver = models.ForeignKey(User,related_name="post_reciver",null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Massage(models.Model):
    massage = models.CharField(max_length=100)
    user = models.ForeignKey(User,related_name="massage_creator")
    post = models.ForeignKey(Post,related_name="post_creator",null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)