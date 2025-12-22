from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),
    path('posts/', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='blog/login.html'), name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('create-post/', views.create_post_simple, name='create_post'),
    path('my-posts/', views.my_posts, name='my_posts'),
    path('edit-post/<int:pk>/', views.edit_post, name='edit_post'),
    path('delete-post/<int:pk>/', views.delete_post, name='delete_post'),
]