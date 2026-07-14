from django import forms
from .models import Book

# Form definition for creating and updating Book instances
class BookForm(forms.ModelForm):
    class Meta:
        # Link this form to the Book model
        model = Book
        
        # Specify the fields to include in the form
        fields = ['title', 'author', 'genre', 'condition', 'price', 'description', 'owner_name']
        
        # Define customizable widgets for custom rendering or attributes
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Tell us more about the book...'}),
            'price': forms.NumberInput(attrs={'step': '0.01'}),
        }

    # Initialize form and apply Bootstrap 5 classes dynamically to all widgets
    def __init__(self, *args, **kwargs):
        super(BookForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            # Check if field uses a ChoiceField widget (like condition)
            if isinstance(field.widget, forms.Select):
                field.widget.attrs.update({'class': 'form-select bg-dark text-white border-secondary'})
            else:
                field.widget.attrs.update({'class': 'form-control bg-dark text-white border-secondary'})
            
            # Add a placeholder matching the help_text or field name
            if field.help_text:
                field.widget.attrs.update({'placeholder': field.help_text})
            else:
                field.widget.attrs.update({'placeholder': f'Enter {field.label.lower()}'})
