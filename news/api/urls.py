from django.urls import path

from . import views

urlpatterns = [
    path('category/', views.CategoryApiList.as_view()),
    path('category/create/', views.CategoryApiCreate.as_view()),
    path('category/<int:pk>/', views.CategoryApiDetail.as_view()),

    path('new/', views.NewApiList.as_view()),
    path('new/create/', views.NewApiCreate.as_view()),
    path('new/<int:pk>/', views.NewApiDetail.as_view()),

    path('comment/', views.CommentApiList.as_view()),
    path('comment/create/', views.CommentApiCreate.as_view()),
    path('comment/<int:pk>/', views.CommentApiDetail.as_view()),
]
