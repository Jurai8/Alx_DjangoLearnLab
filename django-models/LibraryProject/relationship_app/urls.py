"""
URL configuration for LibraryProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .views import list_books, LibraryDetailView, admin_view, librarian_view, member_view, add_book, change_book, delete_book
from django.contrib.auth.views import LoginView, LogoutView

import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('admin/', admin_view, name='admin_view'),
    path('librarian/', librarian_view, name='librarian_view'),
    path('member/', member_view, name='librarian_view'),

    path('all_books/', list_books, name='all_books'),
    path('libraries/books/', LibraryDetailView.as_view(), name='library_books'),
    path('add_book/', add_book, name='add_book'),
    path('edit_book/', change_book, name='change-book'),
    path('delete_book/', delete_book, name='delete_book'),

    path('register/', views.register, name='register'),
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout'), name='logout')
]