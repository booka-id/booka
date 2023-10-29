from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from book.models import Book
from catalogue.forms import BookForm

# Create your views here.
def show_catalogue(request):
    books = Book.objects.all()
    context = {
        'books': books
    }

    return render(request, "admin/catalogue_admin.html", context)

def add_book(request):
    form = BookForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return HttpResponseRedirect(reverse('catalogue:show_catalogue'))

    context = {'form': form}
    return render(request, 'admin/add_book.html', context)