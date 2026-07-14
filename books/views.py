from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from .models import Book
from .forms import BookForm

# 1. Home Page View
# Renders the initial landing welcome page
def home(request):
    return render(request, 'home.html')

# 2. Dashboard View
# Displays total count and list of recently added book listings
def dashboard(request):
    # Retrieve the total count of books in the database
    total_books = Book.objects.count()
    
    # Retrieve the 5 most recently created book listings
    recent_books = Book.objects.all().order_by('-created_at')[:5]
    
    context = {
        'total_books': total_books,
        'recent_books': recent_books
    }
    return render(request, 'dashboard.html', context)

# 3. View All Books (List with Search functionality)
# Displays all book listings and handles searching by title or author
def book_list(request):
    # Fetch the search query from the GET parameters
    query = request.GET.get('q', '')
    
    # If a search query is present, filter the book queryset
    if query:
        books = Book.objects.filter(
            Q(title__icontains=query) | Q(author__icontains=query)
        ).order_by('-created_at')
    else:
        # Otherwise, retrieve all books ordered by creation timestamp (newest first)
        books = Book.objects.all().order_by('-created_at')
        
    context = {
        'books': books,
        'query': query
    }
    return render(request, 'books/list.html', context)

# 4. View Single Book Details View
# Renders detailed page for a single book listing using its ID
def book_detail(request, pk):
    # Fetch the specific book or return a 404 page if not found
    book = get_object_or_404(Book, pk=pk)
    return render(request, 'books/detail.html', {'book': book})

# 5. Add Book View
# Handles the creation of a new book listing
def book_add(request):
    # If the user submitted the form (POST request)
    if request.method == 'POST':
        form = BookForm(request.POST)
        # Validate the form inputs
        if form.is_valid():
            # Save the new book to the database
            form.save()
            # Redirect to the main book listings page
            return redirect('book_list')
    else:
        # If it's a GET request, initialize an empty form
        form = BookForm()
        
    return render(request, 'books/add.html', {'form': form})

# 6. Edit Book View
# Handles updating details of an existing book listing
def book_edit(request, pk):
    # Fetch the specific book to be edited or return 404
    book = get_object_or_404(Book, pk=pk)
    
    # If the user submitted the updated form
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            # Save updates to database
            form.save()
            # Redirect back to the book's detail page
            return redirect('book_detail', pk=book.pk)
    else:
        # Populate the form with the current book details for GET request
        form = BookForm(instance=book)
        
    return render(request, 'books/edit.html', {'form': form, 'book': book})

# 7. Delete Book View
# Handles deleting a book listing after a confirmation page
def book_delete(request, pk):
    # Fetch the specific book to be deleted or return 404
    book = get_object_or_404(Book, pk=pk)
    
    # If user confirms deletion (POST request)
    if request.method == 'POST':
        book.delete()
        # Redirect back to the book listings page
        return redirect('book_list')
        
    # Render confirmation page for GET request
    return render(request, 'books/delete.html', {'book': book})
