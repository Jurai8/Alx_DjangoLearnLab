from django.urls import path
from .views import ListView, CreateView, DeleteView, DetailView, UpdateView

urlpatterns = [
    path('books/', ListView.as_view()),
    path('books/<int:pk>/', DeleteView.as_view()),
    path('books/create/', CreateView.as_view()),
    path('books/delete', DetailView.as_view()),
    path('books/update', UpdateView.as_view())
]