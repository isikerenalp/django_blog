from django import forms
from . import models

class CreateCategory(forms.ModelForm):
    class Meta:
        model = models.Category
        fields = ['name', 'slug']

class CreatePost(forms.ModelForm):
    class Meta:
        model = models.Post
        fields = ['title', 'body', 'slug', 'image', 'category']

class CommentForm(forms.ModelForm):
    class Meta:
        model = models.Comment
        fields = ['text']
