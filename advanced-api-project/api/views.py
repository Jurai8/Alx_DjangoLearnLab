from django.shortcuts import render
from models import Book
from serializers import BookSerializer
from rest_framework import generics
from rest_framework.permissions import IsAdminUser, IsAuthenticated, IsAuthenticatedOrReadOnly


# Create your views here.

class ListView(generics.ListAPIView):
    """
    retrieves all books.
    allow authenticated and non authenticated user to retrieve all books
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = IsAuthenticatedOrReadOnly


class DetailView(generics.RetrieveAPIView):
    """
    retrieves all books.
    allow authenticated and non authenticated user to a
    specific book books
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = IsAuthenticatedOrReadOnly
    

class CreateView(generics.CreateAPIView):
    """
    adds a new book
    allow authenticated users to create a book
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = IsAuthenticated



class UpdateView(generics.UpdateAPIView):
    """
    modifies an existing book
    allow authenticated users to update a book
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = IsAuthenticated

class DeleteView(generics.DestroyAPIView):
    """
    removes a book
    allow authenticated users to remove a book
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = IsAuthenticated

    