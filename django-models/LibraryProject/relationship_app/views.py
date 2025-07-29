from django.shortcuts import render
from django.http import HttpResponse
from models import Book, Library
from django.views.generic.list import ListView




# Create your views here.
def book_list(request):
    books = Book.objects.all()
    context = {'book_list': books }

    return render(request, 'books/book_list.html', context)


class LibraryBookListView(ListView):
    template_name = 'books/book_list.html'
    model = Book
    context_object_name = 'books'

    def get_queryset(self):
        library_name = "Sea Point Library" # Hardcoding for this specific view

        try:
            # Get the specific Library instance
            lib_instance = Library.objects.get(name=library_name)
        
            return lib_instance.books.all()
        except Library.DoesNotExist:
            
            return Book.objects.none() 


