from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect, JsonResponse
from django.http import HttpResponse, HttpResponseNotFound
from django.core import serializers
from django.urls import reverse
from book.models import Book
from catalogue.models import BookStock
from catalogue.forms import BookForm, BookStockForm, AddBookForm

# Create your views here.
def get_catalogue(request):
    books = Book.objects.all()
    book_stocks = BookStock.objects.all()
    context = {
        'books': books,
        'book_stocks' : book_stocks,
    }
    return render(request, 'catalogue.html', context)

def show_catalogue(request):
    books = Book.objects.all()
    b = BookStock.objects.all()
    context = {
        'books': books,
        'tes' : b
    }
    return render(request, "catalogue.html", context)



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

@csrf_exempt
def add_book_ajax(request):
    if request.method == 'POST':
        
        # Dapatkan data dari request
        print(request.POST)
        isbn = request.POST.get('bookISBN')
        print(isbn)
        if not isbn:
            # Handle error: ISBN is required
            return JsonResponse({"error": "ISBN is required"}, status=400)
        title = request.POST.get('bookTitle')
        author = request.POST.get('bookAuthor')
        year = request.POST.get('bookYear')
        publisher = request.POST.get('bookPublisher')
        image_url_large = request.POST.get('bookImageURLLarge')
        quantity = request.POST.get('bookQuantity')
        price = request.POST.get('bookPrice')
        # Membuat instance model buku baru
        new_book = Book.objects.create(
            title=title,
            isbn=isbn,
            author=author,
            year=year,
            publisher=publisher,
            image_url_small=image_url_large,  # Menggunakan image_url_large
            image_url_medium=image_url_large, # Menggunakan image_url_large
            image_url_large=image_url_large
        )
        print("a")
        print(new_book.title)

        # Membuat instance model BookStock baru terkait dengan buku
        new_book_stock = BookStock.objects.create(
            book=new_book,
            quantity=quantity,
            price=price
        )

        return HttpResponse(b"CREATED", status=201)
        

    return HttpResponseNotFound()

@login_required(login_url='/login')
def detail_book(request, pk):
    book_stock = get_object_or_404(BookStock, pk=pk)
    book = book_stock.book
    context = {
        'id': book.id,
        'title': book.title,
        'author': book.author,
        'year': book.year,
        'publisher': book.publisher,
        'isbn': book.isbn,
        'image_url_large': book.image_url_large,
        'price': book_stock.price,
        'quantity': book_stock.quantity
    }
    return render(request, 'detail_book.html', context)

@login_required(login_url='/login')
def buy_book(request, pk):
    book = get_object_or_404(BookStock, pk=pk)
    context= {'book' : book}
    return render(request, 'user/payment.html', context)

@login_required(login_url='/login')
def pay_book(request, pk):
    book = get_object_or_404(BookStock, pk=pk)
    if request.method == 'POST':
        payment_method = request.POST.get('payment_method')
        amount = 1
        book.quantity -= amount
        book.save()
        return redirect('catalogue:show_catalogue')

def delete_book(request, pk):
    if request.method == "POST":
        book = get_object_or_404(Book, pk=pk)
        print("aa")
        book_stock = get_object_or_404(BookStock, book=book)
        print("bbbb")
        book.delete()
        book_stock.delete()
        return JsonResponse({'status': 'success', 'message': 'Buku berhasil dihapus.'})
    

def show_json(request):
    data = BookStock.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

@login_required(login_url='/login')
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

def get_book_json(request):
    book_item = Book.objects.all()
    return HttpResponse(serializers.serialize('json', book_item))

def get_bookstock_json(request):
    bookstock_item = BookStock.objects.all()
    return HttpResponse(serializers.serialize('json', bookstock_item))

def search_book(request):
    if 'search_query' in request.GET:
        search_query = request.GET['search_query']
        results = list(Book.objects.filter(title__icontains=search_query).values('pk', 'title', 'author', 'image_url_large'))
        return JsonResponse(results, safe=False)

    return JsonResponse([], safe=False)

def search_books(request):
    query = request.GET.get('query', '')
    books = Book.objects.filter(title__icontains=query).select_related('bookstock')
    books_data = [
        {
            'id': book.id,
            'title': book.title,
            'author': book.author,
            'year': book.year,
            'publisher': book.publisher,
            'isbn': book.isbn,
            'image_url_large': book.image_url_large,
            'price': book.bookstock.price,
            'quantity': book.bookstock.quantity
        } 
        for book in books
    ]
    print(books_data)
    return JsonResponse(books_data, safe=False)


def get_books_with_stock(request):
    books_with_stock = [
        {
            'id': book.id,
            'title': book.title,
            'author': book.author,
            'year': book.year,
            'publisher': book.publisher,
            'isbn': book.isbn,
            'image_url_large': book.image_url_large,
            'price': book.bookstock.price,
            'quantity': book.bookstock.quantity
        } 
        for book in Book.objects.select_related('bookstock').all()
    ]
    return JsonResponse(books_with_stock, safe=False)


def tes_satu(request):
    print("ayam")
