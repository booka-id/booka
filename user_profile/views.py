from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from user_profile.models import User
from django.http import HttpResponse, JsonResponse
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
import json
from django.db.models import Q

@login_required
def show_profile(request):
     context = {
          'user': request.user
     }
     return render(request, 'profile.html', context=context)

@csrf_exempt
def add_favorite_book(request):
    if request.method == "POST":
        user_email = request.POST.get("email")
        json_data = request.POST.get("json_data")

        # You may want to validate the user and JSON data here.
        # For example, check if the user exists and if the JSON data is in the correct format.

        user_profile = get_object_or_404(User, email=user_email)
        user_profile.favorite_book = json_data
        user_profile.save()

        return JsonResponse({'message': 'success'})

    return JsonResponse({'error': 'Invalid request method'})

@csrf_exempt
def add_wishlist(request):
    if request.method == "POST":
        print(request.POST)
        user_email = request.POST.get("email")
        json_data = request.POST.get("json_data")
        
        # You may want to validate the user and JSON data here.
        # For example, check if the user exists and if the JSON data is in the correct format.

        user_profile = get_object_or_404(User, email=user_email)
        user_profile.wishlist = json_data
        user_profile.save()

        return JsonResponse({'message': 'success'})

    return JsonResponse({'error': 'Invalid request method'})

@csrf_exempt
def get_favorite_book(request, user_email):
    if request.method == "GET":
        # You may want to validate the user and perform any necessary checks here.
        # For example, check if the user exists or has a favorite book.

        user_profile = get_object_or_404(User, email=user_email)

        if user_profile.favorite_book:
            favorite_book = user_profile.favorite_book
            return JsonResponse({'book': favorite_book})

    return JsonResponse({})

@csrf_exempt
def get_wishlist(request, user_email):
    if request.method == "GET":
        # You may want to validate the user and perform any necessary checks here.
        # For example, check if the user exists or has a favorite book.

        user_profile = get_object_or_404(User, email=user_email)

        if user_profile.wishlist:
            favorite_book = user_profile.wishlist
            return JsonResponse({'book': favorite_book})
        
    return JsonResponse({})


@csrf_exempt
def get_user_by_username(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body.decode('utf-8'))
            username = data.get('username', '')  # Extract the 'title' parameter

            # Perform your query based on 'title'
            data = User.objects.filter(username__icontains=username)[:10]

            return JsonResponse(list(data.values()), safe=False, content_type="application/json")
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400, content_type="application/json")
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=400, content_type="application/json")
@csrf_exempt
def user_profile_page(request, username):
    user = get_object_or_404(User, username=username)
    # Replace 'user_profile_template.html' with the actual template for the user profile
    return render(request, 'visiting_profile.html', {'user': user})
# Create your views here.
