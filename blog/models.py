# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from mdeditor.fields import MDTextField
from django.contrib.auth.models import User

class UserProfile(User):
    cname = models.CharField("user name", max_length=30)

class Category(models.Model):
    name = models.CharField('Name',max_length=16)

    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField('Name',max_length=16)

    def __str__(self):
        return self.name

class Blog(models.Model):
    title = models.CharField('Title',max_length=32)
    author = models.CharField('Author',max_length=16)
    abstract = models.TextField('Abstract')
    content = MDTextField()
    created = models.DateTimeField('Publish Time', auto_now_add=True)

    category = models.ForeignKey(Category, verbose_name='Category', on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag, verbose_name='Tags')

    def __str__(self):
        return self.title

class Comment(models.Model):
    blog = models.ForeignKey(Blog, verbose_name='Blog', on_delete=models.CASCADE)

    name = models.CharField('Name', max_length=16)
    email = models.EmailField('Email')
    content = models.CharField('Content', max_length=140)
    created = models.DateTimeField('Publish Time', auto_now_add=True)

    def __str__(self):
        return self.name
