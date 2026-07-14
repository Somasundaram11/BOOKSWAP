from django.urls import path
from . import views

urlpatterns = [
    # Home Page URL route (e.g. localhost:8000/)
    path('', views.home, name='home'),
    
    # Dashboard URL route (e.g. localhost:8000/dashboard/)
    path('dashboard/', views.dashboard, name='dashboard'),
    
    # Book List page showing all books and supporting search (e.g. localhost:8000/books/)
    path('books/', views.book_list, name='book_list'),
    
    # Add new book route (e.g. localhost:8000/books/add/)
    path('books/add/', views.book_add, name='book_add'),
    
    # View single book detail route (e.g. localhost:8000/books/1/)
    path('books/<int:pk>/', views.book_detail, name='book_detail'),
    
    # Edit single book route (e.g. localhost:8000/books/1/edit/)
    path('books/<int:pk>/edit/', views.book_edit, name='book_edit'),
    
    # Delete single book confirmation and action route (e.g. localhost:8000/books/1/delete/)
    path('books/<int:pk>/delete/', views.book_delete, name='book_delete'),
]
