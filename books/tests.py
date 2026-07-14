from decimal import Decimal
from django.test import TestCase
from django.urls import reverse
from .models import Book
from .forms import BookForm

# Test cases for the Book model
class BookModelTest(TestCase):
    def setUp(self):
        # Create a sample book for testing
        self.book = Book.objects.create(
            title="The Hobbit",
            author="J.R.R. Tolkien",
            genre="Fantasy",
            condition="Good",
            price=Decimal("15.99"),
            description="A great classic fantasy story.",
            owner_name="Bilbo Baggins"
        )

    def test_book_creation(self):
        # Test that model fields save correctly
        self.assertEqual(self.book.title, "The Hobbit")
        self.assertEqual(self.book.author, "J.R.R. Tolkien")
        self.assertEqual(self.book.genre, "Fantasy")
        self.assertEqual(self.book.condition, "Good")
        self.assertEqual(self.book.price, Decimal("15.99"))
        self.assertEqual(self.book.description, "A great classic fantasy story.")
        self.assertEqual(self.book.owner_name, "Bilbo Baggins")
        self.assertEqual(str(self.book), "The Hobbit")

# Test cases for views and CRUD flows
class BookViewsTest(TestCase):
    def setUp(self):
        # Set up a few books for testing views
        self.book1 = Book.objects.create(
            title="Django for Beginners",
            author="William S. Vincent",
            genre="Tech",
            condition="New",
            price=Decimal("29.99"),
            description="A build-oriented book.",
            owner_name="John Doe"
        )
        self.book2 = Book.objects.create(
            title="Two Towers",
            author="J.R.R. Tolkien",
            genre="Fantasy",
            condition="Good",
            price=Decimal("12.50"),
            description="Second volume of Lord of the Rings.",
            owner_name="Jane Doe"
        )

    def test_home_view(self):
        # Test that the home page renders with status 200
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')

    def test_dashboard_view(self):
        # Test that the dashboard renders with status 200 and passes correct context
        response = self.client.get(reverse('dashboard'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'dashboard.html')
        self.assertEqual(response.context['total_books'], 2)
        self.assertEqual(len(response.context['recent_books']), 2)

    def test_book_list_view_all(self):
        # Test book listing page displays all books
        response = self.client.get(reverse('book_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'books/list.html')
        self.assertEqual(len(response.context['books']), 2)

    def test_book_list_view_search_match(self):
        # Test search query filters books correctly
        response = self.client.get(reverse('book_list'), {'q': 'Django'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['books']), 1)
        self.assertEqual(response.context['books'][0].title, "Django for Beginners")

    def test_book_list_view_search_no_match(self):
        # Test search query with no matching items
        response = self.client.get(reverse('book_list'), {'q': 'Python'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['books']), 0)

    def test_book_detail_view(self):
        # Test single book detail page
        response = self.client.get(reverse('book_detail', args=[self.book1.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'books/detail.html')
        self.assertContains(response, "Django for Beginners")

    def test_book_add_view_get(self):
        # Test add page renders correctly
        response = self.client.get(reverse('book_add'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'books/add.html')
        self.assertIsInstance(response.context['form'], BookForm)

    def test_book_add_view_post_valid(self):
        # Test submitting a valid new book listing redirects and saves it
        data = {
            'title': 'New Book Title',
            'author': 'New Author',
            'genre': 'Fiction',
            'condition': 'Fair',
            'price': 9.99,
            'description': 'A fresh listing.',
            'owner_name': 'Alice Smith'
        }
        response = self.client.post(reverse('book_add'), data)
        self.assertEqual(response.status_code, 302) # Redirect status code
        self.assertEqual(Book.objects.count(), 3)
        self.assertTrue(Book.objects.filter(title='New Book Title').exists())

    def test_book_edit_view_get(self):
        # Test edit page rendering pre-populated with instance
        response = self.client.get(reverse('book_edit', args=[self.book1.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'books/edit.html')
        self.assertContains(response, "Django for Beginners")

    def test_book_edit_view_post_valid(self):
        # Test editing book saves updates
        data = {
            'title': 'Django for Beginners (Updated)',
            'author': 'William S. Vincent',
            'genre': 'Tech & Programming',
            'condition': 'New',
            'price': 34.99,
            'description': 'An updated build-oriented book.',
            'owner_name': 'John Doe'
        }
        response = self.client.post(reverse('book_edit', args=[self.book1.pk]), data)
        self.assertEqual(response.status_code, 302)
        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, 'Django for Beginners (Updated)')
        self.assertEqual(self.book1.genre, 'Tech & Programming')
        self.assertEqual(self.book1.price, Decimal("34.99"))

    def test_book_delete_view_get(self):
        # Test delete confirmation page renders correctly
        response = self.client.get(reverse('book_delete', args=[self.book1.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'books/delete.html')

    def test_book_delete_view_post(self):
        # Test deleting a book removes it from the database
        response = self.client.post(reverse('book_delete', args=[self.book1.pk]))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Book.objects.count(), 1)
        self.assertFalse(Book.objects.filter(pk=self.book1.pk).exists())
