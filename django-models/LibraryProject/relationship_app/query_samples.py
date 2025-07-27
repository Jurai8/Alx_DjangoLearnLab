from models import Author, Book, Library, Librarian

# Query all books by a specific author
Herbert_books = Book.objects.filter(author__name='Herbert')

# List all books in a library.
library = Library.objects.get(name="library_name")
all_books = library.books.all()

# Retrieve the librarian for a library.
librarian = Librarian.get(library__name="library_name")
