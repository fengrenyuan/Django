# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-01-15 03:52
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32, verbose_name='Title')),
                ('author', models.CharField(max_length=16, verbose_name='Author')),
                ('content', models.TextField(verbose_name='Content')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Publish Time')),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=16, verbose_name='Name')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=16, verbose_name='Name')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('content', models.CharField(max_length=140, verbose_name='Content')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Publish Time')),
                ('blog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Blog', verbose_name='Blog')),
            ],
        ),
        migrations.RemoveField(
            model_name='article',
            name='author',
        ),
        migrations.RemoveField(
            model_name='article',
            name='classification',
        ),
        migrations.RemoveField(
            model_name='article',
            name='tags',
        ),
        migrations.RemoveField(
            model_name='tag',
            name='create_time',
        ),
        migrations.RemoveField(
            model_name='tag',
            name='tag_name',
        ),
        migrations.AddField(
            model_name='tag',
            name='name',
            field=models.CharField(default='null', max_length=16, verbose_name='Name'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Article',
        ),
        migrations.DeleteModel(
            name='Author',
        ),
        migrations.DeleteModel(
            name='Classification',
        ),
        migrations.AddField(
            model_name='blog',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Category', verbose_name='Category'),
        ),
        migrations.AddField(
            model_name='blog',
            name='tags',
            field=models.ManyToManyField(to='blog.Tag', verbose_name='Tags'),
        ),
    ]
