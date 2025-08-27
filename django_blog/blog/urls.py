from django.urls import path
from views import RegistrationView, LoginView, LogoutView, profile_view, PostListView, PostCreateView, PostDetailView, PostUpdateView, PostDeleteView

urlpatterns = [
    path('register/', RegistrationView.as_view(), name='register'),
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('profile/', profile_view, name='profile'),

    path('posts/', PostListView.as_view(template_name='all-posts.html'), name='posts'),
    path('posts/new/', PostCreateView.as_view(template_name='create_posts.html'), name='create_post'),
    path('posts/<int:pk>/', PostDetailView.as_view(template_name='post_detail.html'), name='post-details'),
    path('posts/<int:pk>/edit/', PostUpdateView.as_view(template_name='edit_post.html'), name='edit-post'),
    path('posts/<int:pk>/delete/', PostDeleteView.as_view(), name='delete-post')

]