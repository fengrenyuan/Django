# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.db.models.aggregates import Count
from django.db.models import Q
from django.http import Http404
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage, InvalidPage
from .models import Blog, Comment, Tag, Category
from .forms import CommentForm, BlogForm
import datetime
import markdown

def get_day():
    now = datetime.datetime.now()
    old = datetime.datetime(2018,6,9)
    interval = now - old
    day = interval.days
    return day

def home(request):
    return render(request, 'index.html')

def get_blogs(request, page):
    if not page:
        page = 1
    day = get_day()
    categorys = Category.objects.annotate(num_blogs=Count('blog')).filter(num_blogs__gt=0)
    blogs = Blog.objects.all().order_by('-created')
    paginator = Paginator(blogs, 5)

    try:
        blog_page = paginator.page(page)
    except PageNotAnInteger:
        page = 1
        blog_page = paginator.page(page)
    except InvalidPage:
        raise Http404
    except EmptyPage:
        page = paginator.num_pages
        blog_page = paginator.page(page)

    ctx = {
        'categorys': categorys,
        'blogs': blog_page,
        'day': day,
        'pagerange': paginator.page_range,
        'currentpage': page
    }
    return render(request, 'blog-list.html', ctx)

def get_detail(request, blog_id):
    day = get_day()
    categorys = Category.objects.annotate(num_blogs=Count('blog')).filter(num_blogs__gt=0)
    try:
        blog = Blog.objects.get(id=blog_id)
        blog.content = markdown.markdown(blog.content,extensions=[
                                        'markdown.extensions.extra', 
                                        'markdown.extensions.codehilite', 
                                        'markdown.extensions.toc', 
                                        ])
    except Blog.DoesNotExist:
        raise Http404

    if request.method == 'GET':
        form = CommentForm()
    else:
        form = CommentForm(request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            cleaned_data['blog'] = blog
            Comment.objects.create(**cleaned_data)

    ctx = {
        'categorys': categorys,
        'blog': blog,
        'comments': blog.comment_set.all().order_by('-created'),
        'form': form,
        'day': day
    }
    return render(request, 'blog-detail.html', ctx)

def get_blog(request, page):
    if not page:
        page = 1
    day = get_day()
    categorys = Category.objects.annotate(num_blogs=Count('blog')).filter(num_blogs__gt=0)
    if request.method == 'GET':
        cat_id = request.GET.get('cat')
        author_name = request.GET.get('author')
        tag_id = request.GET.get('tag')
    if cat_id:
        try:
            blogs = Blog.objects.filter(category=cat_id)
        except Blog.DoesNotExist:
            raise Http404
    elif author_name:
        try:
            blogs = Blog.objects.filter(author=author_name)
        except Blog.DoesNotExist:
            raise Http404
    elif tag_id:
        try:
            blogs = Blog.objects.filter(tags=tag_id)
        except Blog.DoesNotExist:
            raise Http404
    else:
            raise Http404

    paginator = Paginator(blogs, 5)
    try:
        blog_page = paginator.page(page)
    except PageNotAnInteger:
        page = 1
        blog_page = paginator.page(page)
    except InvalidPage:
        raise Http404
    except EmptyPage:
        page = paginator.num_pages
        blog_page = paginator.page(page)

    ctx = {
        'categorys': categorys,
        'blogs': blog_page,
        'day': day,
        'pagerange': paginator.page_range,
        'currentpage': page
    }
    return render(request, 'blog-list.html', ctx)

def create_blog(request):
    day = get_day()
    categorys = Category.objects.annotate(num_blogs=Count('blog')).filter(num_blogs__gt=0)
    tags = Tag.objects.all()
    cats = Category.objects.all()
    if request.method == 'GET':
        form = BlogForm()
    else:
        form = BlogForm(request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            cat_name = request.POST.get('cat')
            cat_obj = Category.objects.get(name=cat_name)
            tag_names = request.POST.getlist('tags')
            cleaned_data['category'] = cat_obj
            #cleaned_data['tags'] = tags
            
            blog = Blog.objects.create(**cleaned_data)
            for tag_name in tag_names:
                tag_obj = Tag.objects.get(name=tag_name)
                blog.tags.add(tag_obj)

    ctx = {
        'categorys': categorys,
        'tags': tags,
        'cats': cats,
        'form': form,
        'day': day
    }
    return render(request, 'blog-create.html', ctx)

def search_blog(request, page):
    if not page:
        page = 1
    day = get_day()
    categorys = Category.objects.annotate(num_blogs=Count('blog')).filter(num_blogs__gt=0)
    q = request.GET.get('search')
    if not q:
        ctx = {
            'categorys': categorys,
            'blogs': Blog.objects.all().order_by('-created'),
            'day': day
        }
        return render(request, 'blog-list.html', ctx)

    blogs = Blog.objects.filter(Q(title__icontains=q) | Q(content__icontains=q))
    paginator = Paginator(blogs, 5)
    try:
        blog_page = paginator.page(page)
    except PageNotAnInteger:
        page = 1
        blog_page = paginator.page(page)
    except InvalidPage:
        raise Http404
    except EmptyPage:
        page = paginator.num_pages
        blog_page = paginator.page(page)

    ctx = {
        'categorys': categorys,
        'blogs': blog_page,
        'day': day,
        'pagerange': paginator.page_range,
        'currentpage': page
    }
    return render(request, 'blog-list.html', ctx)
