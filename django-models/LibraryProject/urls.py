from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    # Book-related URLs with permission requirements
    path('books/', views.list_books, name='list_books'),
    path('books/add/', views.add_book, name='add_book'),  # Requires can_add_book permission
    path('books/edit/<int:book_id>/', views.edit_book, name='edit_book'),  # Requires can_change_book permission
    path('books/delete/<int:book_id>/', views.delete_book, name='delete_book'),  # Requires can_delete_book permission
    
    # Library-related URLs
    path('library/<int:library_id>/', views.library_detail, name='library_detail'),
    
    # Authentication URLs
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='registration/logout.html'), name='logout'),
    path('register/', views.register, name='register'),
]
