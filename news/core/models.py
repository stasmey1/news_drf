from django.contrib.auth.models import User
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name[:20]


class New(models.Model):
    title = models.CharField(max_length=100, null=True, blank=True)
    text = models.TextField(max_length=1000, null=True, blank=True)
    time_create = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, related_name='news')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='news', null=True, blank=True)
    generate = models.BooleanField(default=False)

    def __str__(self):
        return self.title[:20]


class Comment(models.Model):
    text = models.TextField(max_length=1000, null=True, blank=True)
    time_create = models.DateTimeField(auto_now_add=True)
    new = models.ForeignKey(New, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments', null=True, blank=True)
