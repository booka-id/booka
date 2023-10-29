from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from user_profile.models import User
from django.http import HttpResponse, JsonResponse
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
import json

@login_required
def show_profile(request):
     context = {
          'user': request.user
     }
     return render(request, 'profile.html', context=context)


def add_favorite_book(request):
    if request.method == "POST":
        user_email = request.POST.get("email")
        json_data = request.POST.get("json_data")

        # You may want to validate the user and JSON data here.
        # For example, check if the user exists and if the JSON data is in the correct format.

        user_profile = get_object_or_404(User, email=user_email)
        user_profile.favorite_book = json_data
        user_profile.save()

        return JsonResponse({'message': 'Favorite book added successfully'})

    return JsonResponse({'error': 'Invalid request method'})

@csrf_exempt
def get_favorite_book(request, user_email):
    if request.method == "GET":
        # You may want to validate the user and perform any necessary checks here.
        # For example, check if the user exists or has a favorite book.

        user_profile = get_object_or_404(User, email=user_email)

        if user_profile.favorite_book:
            favorite_book = user_profile.favorite_book
            return JsonResponse({'favorite_book': favorite_book})

    return JsonResponse({})
# Create your views here.
