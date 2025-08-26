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
from django.urls import reverse




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

@login_required
def profile_view(request):
    """
    A view that allows an authenticated user to view and edit their profile details.
    This view handles both GET and POST requests.
    """
    # Get the user's profile object
    profile = request.user.profile

    # This is where we explicitly check the request method
    # It will be 'POST' if the form was submitted
    if request.method == 'POST':
        # If it's a POST request, we pass the data from the form
        form = ProfileForm(request.POST, instance=profile)

        # Check if the form is valid
        if form.is_valid():
            # Save the updated profile data
            form.save()
            
            # Manually update the user's email from the form data
            request.user.email = form.cleaned_data['email']
            request.user.save()

            # Redirect to a success page
            return redirect(reverse('profile_success_page'))
    else:
        # If it's a GET request, we create a form pre-populated with the
        # user's existing profile data.
        form = ProfileForm(instance=profile)

    # Render the template with the form
    return render(request, 'profile.html', {'form': form})


    
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