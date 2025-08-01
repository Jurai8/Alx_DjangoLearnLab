from django.shortcuts import render, redirect
from django.http import HttpResponse
from models import Book, Library
from .models import Library
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth import login
from django.contrib.auth import logout




# Create your views here.
def list_books(request):
    books = Book.objects.all()
    context = {'book_list': books }

    return render(request, 'relationship_app/list_books.html', context)


class LibraryDetailView(ListView):
    template_name = 'relationship_app/library_detail.html'
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


class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'relationship_app/signup.html'


def register(request):
    """
    A function-based view to handle user registration.
    """
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Optional: Log the user in immediately after registration
            # login(request, user)
            return redirect(reverse_lazy('login')) # Redirect to the login page
    else:
        form = UserCreationForm()

    context = {'form': form, 'template_name': 'relationship_app/signup.html'}
    return render(request, 'relationship_app/signup.html', context)



