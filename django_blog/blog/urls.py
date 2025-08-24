from django.urls import path
from views import RegistrationView, LoginView, LogoutView, ProfileView

urlpatterns = [
    path('register/', RegistrationView.as_view(), name='register'),
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('profile/', ProfileView.as_view(template_name='profile.html'), name='profile')
]