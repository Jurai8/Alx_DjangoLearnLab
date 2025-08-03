from django.shortcuts import render
from models import CustomUser
from django.contrib.auth.decorators import permission_required


# Create your views here.

@permission_required('bookshelf.can_view', raise_exception=True)
def view_user(request):
    pass

@permission_required('bookshelf.can_create', raise_exception=True)
def create_user(request):
    pass

@permission_required('bookshelf.can_edit', raise_exception=True)
def edit_user(request):
    pass

@permission_required('bookshelf.can_delete', raise_exception=True)
def delete_user(request):
    pass