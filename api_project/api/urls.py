
from django.contrib import admin
from django.urls import path, include
from views import BookList
from rest_framework import routers


urls = [
    path('book/', BookList.as_view(), name='book-list'),
]