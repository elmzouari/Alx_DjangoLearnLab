from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import permission_required
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseForbidden
from .models import Book, Author, Library, Librarian
from .forms import BookForm

def list_books(request):
    """View to list all books - no special permissions required"""
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})

@permission_required('relationship_app.can_add_book', raise_exception=True)
def add_book(request):
    """View to add a new book - requires can_add_book permission"""
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_books')
    else:
        form = BookForm()
    
    return render(request, 'relationship_app/add_book.html', {'form': form})

@permission_required('relationship_app.can_change_book', raise_exception=True)
def edit_book(request, book_id):
    """View to edit an existing book - requires can_change_book permission"""
    book = get_object_or_404(Book, pk=book_id)
    
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('list_books')
    else:
        form = BookForm(instance=book)
    
    return render(request, 'relationship_app/edit_book.html', {'form': form, 'book': book})

@permission_required('relationship_app.can_delete_book', raise_exception=True)
def delete_book(request, book_id):
    """View to delete a book - requires can_delete_book permission"""
    book = get_object_or_404(Book, pk=book_id)
    
    if request.method == 'POST':
        book.delete()
        return redirect('list_books')
    
    return render(request, 'relationship_app/delete_book.html', {'book': book})

def library_detail(request, library_id):
    """View to display library details"""
    library = get_object_or_404(Library, pk=library_id)
    return render(request, 'relationship_app/library_detail.html', {'library': library})

def register(request):
    """User registration view"""
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('list_books')
    else:
        form = UserCreationForm()
    
    return render(request, 'registration/register.html', {'form': form})
