from django.shortcuts import render
from rest_framework import generics
from models import Book
from serializers import BookSerializer

# Create your views here.
class BookList(generics.ListAPIView):
    "Returns a list of all the books"

    queryset = Book.objects.all()
    serializer_class = BookSerializer