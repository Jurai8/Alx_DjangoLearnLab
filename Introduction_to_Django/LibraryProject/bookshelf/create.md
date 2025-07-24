# CRUD operations

## CREATE

>>> from bookshelf.models import Book
>>> book_2 = Book(title = "1984", author = "George Orwell", publication_year = "1949")
>>> book_2.save()

### Expected Output

>>>