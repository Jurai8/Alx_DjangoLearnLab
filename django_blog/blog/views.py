from django.shortcuts import render, get_object_or_404, redirect
from .forms import RegistrationForm, ProfileForm
from django.views.generic import ListView, UpdateView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from .models import Profile
from django.contrib.auth.decorators import login_required



# Create your views here.

# auth views
class MyLoginView(LoginView):
    template_name = 'login.html'

class MyLogoutView(LogoutView):
    template_name = 'logout.html'

class RegistrationView(CreateView):
    template_name = 'register.html'
    form_class = RegistrationForm
    success_url = reverse_lazy('success_page')

class ProfileView(LoginRequiredMixin, UpdateView):
    model = Profile
    form_class = ProfileForm
    template_name = 'profile.html'
    success_url = reverse_lazy('profile_success_page')
    
    # We need to override get_object to get the profile of the current user
    def get_object(self, queryset=None):
        return self.request.user.profile
    
    # Override form_valid to handle the user's email update
    def form_valid(self, form):
        # Update the User's email manually
        self.request.user.email = form.cleaned_data['email']
        self.request.user.save()
        
        # Call the parent form_valid to save the Profile model
        return super().form_valid(form)

    
class ListView(ListView):
    pass
class DetailView():
    pass

class CreateView():
    pass

class UpdateView():
    pass

class DeleteView():
    pass