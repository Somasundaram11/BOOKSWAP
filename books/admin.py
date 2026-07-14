from django.contrib import admin
from .models import Book

# Register the Book model with the admin interface
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    # Fields to display in the list view of the admin panel
    list_display = ('title', 'author', 'genre', 'condition', 'price', 'owner_name', 'created_at')
    
    # Fields that should be searchable in the search bar
    search_fields = ('title', 'author', 'owner_name')
    
    # Filter options in the right sidebar of the admin list view
    list_filter = ('condition', 'genre', 'created_at')
    
    # Sort order (newest first by default)
    ordering = ('-created_at',)
