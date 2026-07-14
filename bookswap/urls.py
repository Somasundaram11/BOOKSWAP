from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # Admin URL configuration
    path('admin/', admin.site.urls),
    # Include all book-related URLs from the books app
    path('', include('books.urls')),
]
