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

def show_catalogue(request):
    books = Book.objects.all()
    b = BookStock.objects.all()
    context = {
        'books': books,
        'tes' : b
    }
    if request.user.is_superuser:
        return render(request, "admin/catalogue_admin.html", context)
    
    else:
        return render(request, "user/catalogue_user.html", context)



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

def add_book_ajax(request):
    if request.method == 'POST':
        isbn = request.POST.get("isbn")
        title = request.POST.get("title")
        author = request.POST.get("author")
        year = request.POST.get("year")
        publisher = request.POST.get("publisher")
        image_url_small = request.POST.get("image_url_small")
        image_url_medium = request.POST.get("image_url_medium")
        image_url_large = request.POST.get("image_url_large")
        quantity = request.POST.get("quantit+y")
        price = request.POST.get("price")

        new_book = Book(isbn=isbn, title=title, author=author, year=year, publisher=publisher, image_url_small=image_url_small, image_url_medium=image_url_medium, image_url_large=image_url_large)
        new_book.save()
        new_book_stock = BookStock(book=new_book, quantity=quantity, price=price)
        new_book_stock.save()

        return HttpResponse(b"CREATED", status=201)
    
    return HttpResponseNotFound()
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

@login_required(login_url='/login')
def delete_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    book.delete()
    book = get_object_or_404(BookStock, pk=pk)
    book.delete()
    return HttpResponseRedirect(reverse('catalogue:show_catalogue'))

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
