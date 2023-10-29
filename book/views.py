from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
import json

from book.models import Book

# Create your views here.
def get_books(request):
    data = Book.objects.all()
    return HttpResponse(serializers.serialize("json", data),
    content_type = "application/json")

@csrf_exempt
def get_books_by_title(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body.decode('utf-8'))
            title = data.get('title', '')  # Extract the 'title' parameter

            # Perform your query based on 'title'
            data = Book.objects.filter(title__icontains=title)[:10]

            return JsonResponse(list(data.values()), safe=False, content_type="application/json")
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400, content_type="application/json")
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=400, content_type="application/json")