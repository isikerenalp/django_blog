from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length = 100)
    slug = models.SlugField(max_length=100, unique = True)
    body = models.TextField(max_length=500)
    date = models.DateTimeField(auto_now_add = True)
    image = models.ImageField(default='default.jpg', blank = True)
    author = models.ForeignKey(User, on_delete=models.PROTECT ,default = None)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, default = None)

    def __str__(self):
        return self.title

    def snippet(self):
        return self.body[:50] + '...'

class Comment(models.Model):
    post = models.ForeignKey('posts.Post', on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.PROTECT ,default = None)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text
