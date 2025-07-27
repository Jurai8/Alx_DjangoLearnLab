from models import Author, Book, Library, Librarian

# Query all books by a specific author
Herbert_books = Book.objects.filter(author__name='Herbert')

# List all books in a library.
Library_books = Book.objects.all()

# Retrieve the librarian for a library.
Librarian = Librarian.objects.get('name')