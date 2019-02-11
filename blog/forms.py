from django import forms
from .models import Category, Tag

class CommentForm(forms.Form):
    name = forms.CharField(label='name', max_length=16, error_messages={
        'required': 'Please fill in your name',
        'max_length': 'Name length more than 16'
    })

    email = forms.EmailField(label='email', error_messages={
        'required': 'Please fill in your email',
        'invalid': 'Error email format'
    })

    content = forms.CharField(label='content', max_length=200, error_messages={
        'required': 'Please fill in your content',
        'max_length': 'Content length more than 200'
    })

class BlogForm(forms.Form):
    title = forms.CharField(label='title', max_length=50, error_messages={
        'required': 'Please fill in the title of the blog',
        'max_length': 'Title length more than 50'
    })
    author = forms.CharField(label='author', max_length=16, error_messages={
        'required': 'Please fill in the author name',
        'max_lenght': 'Author name more than 16'
    })
    content = forms.CharField(widget=forms.Textarea, label='content', error_messages={
        'required': 'Please fill in the content'
    })
