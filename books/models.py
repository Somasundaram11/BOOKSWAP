from django.db import models

# Define the Book model representing a book listing in the application
class Book(models.Model):
    # Choices for the book condition field
    CONDITION_CHOICES = [
        ('New', 'New'),
        ('Good', 'Good'),
        ('Fair', 'Fair'),
        ('Old', 'Old'),
    ]

    # Title of the book (max 200 characters)
    title = models.CharField(max_length=200, help_text="Enter the title of the book")
    
    # Author of the book (max 200 characters)
    author = models.CharField(max_length=200, help_text="Enter the author's name")
    
    # Genre of the book (max 100 characters)
    genre = models.CharField(max_length=100, help_text="Enter the book's genre")
    
    # Condition of the book, using the defined choices above
    condition = models.CharField(
        max_length=10, 
        choices=CONDITION_CHOICES, 
        default='Good', 
        help_text="Select the condition of the book"
    )
    
    # Price of the book (supporting up to 10 digits with 2 decimal places)
    price = models.DecimalField(max_digits=10, decimal_places=2, help_text="Enter the price of the book")
    
    # Description of the book (unlimited length text)
    description = models.TextField(help_text="Provide a description of the book")
    
    # Name of the owner who listed the book (max 100 characters)
    owner_name = models.CharField(max_length=100, help_text="Enter your name (owner)")
    
    # Timestamp when the book listing was created (automatically populated)
    created_at = models.DateTimeField(auto_now_add=True)

    # String representation of the model instance (returns the book title)
    def __str__(self):
        return self.title
