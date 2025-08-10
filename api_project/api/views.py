from django.shortcuts import render
from rest_framework import generics, viewsets
from models import Book
from .serializers import BookSerializer

# Create your views here.
class BookList(generics.ListAPIView):
    "Returns a list of all the books"

    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookViewSet(viewsets.ModelViewSet):
    """
    A viewset that provides the standard actions for a Book model.
    It will handle list, create, retrieve, update, and destroy.
    """

    queryset = Book.objects.all()
    serializer_class = BookSerializer