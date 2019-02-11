# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase

from .models import Blog

if __name__ == '__main__':
    tags = Blog.objects.all()
    print tags
