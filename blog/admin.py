# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Category, Tag, Blog

class UserProfileAdmin(admin.ModelAdmin):
    list_dispaly = ('cname', 'username', 'emain')
    search_fields = ('cname', 'username')
admin.site.register([Category, Tag, Blog])
