from rest_framework import serializers

from core.models import Category, New, Comment


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name', ]


class NewSerializer(serializers.ModelSerializer):
    class Meta:
        model = New
        fields = ['category', 'title', 'text', 'generate', ]


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['new', 'text', ]
