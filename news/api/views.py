from rest_framework import generics

from core.models import Category, New, Comment
from .serializers import CategorySerializer, NewSerializer, CommentSerializer
from core.parser import get_data_new_osnmedia_ru


class CategoryApiList(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryApiDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryApiCreate(generics.CreateAPIView):
    serializer_class = CategorySerializer


class NewApiList(generics.ListAPIView):
    queryset = New.objects.all()
    serializer_class = NewSerializer


class NewApiDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = New.objects.all()
    serializer_class = NewSerializer


class NewApiCreate(generics.CreateAPIView):
    serializer_class = NewSerializer

    def perform_create(self, serializer):
        if serializer.validated_data.get('generate'):
            pars_data = get_data_new_osnmedia_ru()
            serializer.validated_data['title'] = pars_data.get('title')
            serializer.validated_data['text'] = pars_data.get('text')
        super().perform_create(serializer)


class CommentApiList(generics.ListAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class CommentApiDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class CommentApiCreate(generics.CreateAPIView):
    serializer_class = CommentSerializer
