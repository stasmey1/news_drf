from django.contrib import admin

from .models import Comment, New, Category

admin.site.register(Comment)
admin.site.register(New)
admin.site.register(Category)
