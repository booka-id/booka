from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.core import serializers
from django.urls import reverse
from book.models import Book
from catalogue.models import BookStock
from catalogue.forms import BookForm, BookStockForm, AddBookForm

# Create your views here.
def show_catalogue(request):
    books = Book.objects.all()
    b = BookStock.objects.all()
    context = {
        'books': books,
        'tes' : b
    }

    return render(request, "admin/catalogue_admin.html", context)

def add_book(request):
    if request.method == 'POST':
        form = AddBookForm(request.POST)
        if form.is_valid():
            # Simpan buku
            book = form.save(commit=False)
            book.save()

            # Simpan informasi tambahan (kuantitas dan harga) dalam BookStock
            quantity = form.cleaned_data['quantity']
            price = form.cleaned_data['price']
            BookStock.objects.create(book=book, quantity=quantity, price=price)
            print("tesss")

            return redirect('catalogue:show_catalogue')
    else:
        form = AddBookForm()

    return render(request, 'admin/add_book.html', {'form': form})
    # book_form = BookForm(request.POST or None)
    # book_stock_form = BookStockForm(request.POST or None)

    # if request.method == "POST":
    #     # Periksa apakah formulir valid
    #     if book_form.is_valid() and book_form.is_valid():
    #         # Simpan kedua formulir
    #         book_form.save()
    #         book_stock_form.save()

    #         # Kembali ke halaman awal atau lakukan tindakan lain yang sesuai
    #         return HttpResponseRedirect(reverse('catalogue:show_catalogue'))
        
    # context = {'book_form': book_form, 'book_stock_form': book_stock_form}
    # return render(request, 'admin/add_book.html', context)

@login_required(login_url='/login')
def detail_book(request, pk):
    book = get_object_or_404(BookStock, pk=pk)
    context = {'book': book}
    return render(request, 'detail_book.html', context)

def buy_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    context= {'book' : book}
    return render(request, 'user/payment.html', context)

def delete_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    book.delete()
    book = get_object_or_404(BookStock, pk=pk)
    book.delete()
    return HttpResponseRedirect(reverse('catalogue:show_catalogue'))

def show_json(request):
    data = BookStock.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def edit_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    book_stock = get_object_or_404(BookStock,pk=pk)

    book_form = BookForm(request.POST or None, instance=book)
    book_stock_form = BookStockForm(request.POST or None, instance=book_stock)

    if request.method == "POST":
        # Periksa apakah formulir valid
        if book_form.is_valid() and book_form.is_valid():
            # Simpan kedua formulir
            book_form.save()
            book_stock_form.save()

            # Kembali ke halaman awal atau lakukan tindakan lain yang sesuai
            return HttpResponseRedirect(reverse('catalogue:show_catalogue'))
        
    context = {'book_form': book_form, 'book_stock_form': book_stock_form}
    
    return render(request, 'admin/edit_book.html', context)