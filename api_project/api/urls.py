
from django.contrib import admin
from django.urls import path, include
from views import BookList, BookViewSet
from rest_framework import routers

router = routers.DefaultRouter()

router.regiser(r'books_all', BookViewSet, basename='book_all')

urls = [
    path('book/', BookList.as_view(), name='book-list'),
    path('', include(router.urls)),
]