from django.urls import path
from .views import ListView, CreateView, DeleteView, DetailView

urlpatterns = [
    path('books/', ListView.as_view()),
    path('books/<int:pk>/', DeleteView.as_view()),
    path('books/create/', CreateView.as_view()),
    path('books/<int:pk>/delete', DetailView.as_view())
]