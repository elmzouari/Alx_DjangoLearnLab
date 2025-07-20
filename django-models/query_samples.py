import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'your_project_name.settings')  # replace with your project name
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

# Query all books by a specific author
author = Author.objects.get(name="J.K. Rowling")
books_by_author = Book.objects.filter(author=author)
print("Books by", author.name, ":", [book.title for book in books_by_author])

# List all books in a library
library = Library.objects.get(name="Central Library")
books_in_library = library.books.all()
print("Books in", library.name, ":", [book.title for book in books_in_library])

# Retrieve the librarian for a library
librarian = Librarian.objects.get(library=library)
print("Librarian of", library.name, ":", librarian.name)
