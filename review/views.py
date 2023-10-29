from django.http import HttpResponse, HttpResponseRedirect,HttpResponseNotFound
from django.core import serializers
from django.shortcuts import render
from django.urls import reverse
from book.models import Book
from django.contrib.auth.decorators import login_required
from user_profile.models import User
from .models import Review
from .forms import ReviewForm
from django.views.decorators.csrf import csrf_exempt
from urllib.parse import unquote
from django.db.models import Count


# Create your views here.
def get_reviews(request):
    reviews = Review.objects.all()
    books = Book.objects.all()
    top_books = Book.objects.annotate(num_reviews=Count('review')).order_by('-num_reviews')[:10]
    authors = {book.author for book in books}
    authors = list(authors)
    authors.sort()
    context = {
        'reviews' : reviews,
        'books' : books,
        'authors' : authors,
        'top_books' : top_books,
    }
    return render(request, 'main.html', context)

def see_review(request, id):
    book = Book.objects.get(pk=id)
        
    context = {
        'book':book,
        'user': request.user
    }
    return render(request, 'see_review.html', context)

@login_required
def write_review(request, book_id):
    book = Book.objects.get(pk=book_id)
    context = {
        'book':book,
        'user': request.user
    }
    return render(request, 'write_review.html', context)

def get_all_reviews(request):
    reviews = Review.objects.all()
    return HttpResponse(serializers.serialize('json', reviews), content_type="application/json")

def get_reviews_by_id(request, id):
    book = Book.objects.get(pk=id)
    reviews = Review.objects.filter(book=book)
    return HttpResponse(serializers.serialize('json', reviews), content_type="application/json")

def get_reviews_by_user(request,user_id):
    reviews = Review.objects.filter(user=user_id)
    return HttpResponse(serializers.serialize('json', reviews), content_type="application/json")

def get_user(request, id):
    user = User.objects.filter(pk=id)
    return HttpResponse(serializers.serialize('json', user), content_type="application/json")

def post_review(request, book_id):
    book = Book.objects.get(pk=book_id)
    if request.method == 'POST':
        title = request.POST.get("title")
        content = request.POST.get("content")
        rating = request.POST.get("rating")
        user = request.user

        new_review = Review(
            title=title,
            content=content,
            rating=rating,
            user=user,
            book=book,
        )
        new_review.save()
        url = '/review/'+ str(book_id)
        return HttpResponse()
    
    return HttpResponseNotFound()

@csrf_exempt
def delete_review(request,review_id):
    if request.method=='DELETE':
        review = Review.objects.get(pk=review_id)
        review.delete()

        return HttpResponse(b'DELETED', status=200)
    return HttpResponseNotFound()

def get_books_by_author(request,author):
    filteredBooks = Book.objects.filter(author=unquote(author))
    return HttpResponse(serializers.serialize('json', filteredBooks), content_type='application/json')

def get_books_by_id(request,book_id):
    filteredBooks = Book.objects.filter(pk=book_id)
    return HttpResponse(serializers.serialize('json', filteredBooks), content_type='application/json')

def get_ranks(request):
    top_books = Book.objects.annotate(num_reviews=Count('review')).order_by('-num_reviews')[:10]
    return HttpResponse(serializers.serialize('json', top_books), content_type='application/json')
