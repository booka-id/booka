from user_profile.forms import RegisterForm, ChangeForm
from user_profile.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages  
import datetime, json
from django.http import HttpResponseRedirect, JsonResponse
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers

@csrf_exempt
def show_home(request):  
    if request.user.is_authenticated:
        user = request.user.username
    else:
        user = 'guest'

    context ={
        'user': user,
    }
    return render(request, "home.html", context=context)

@csrf_exempt
def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            response = HttpResponseRedirect(reverse("home:show_home")) 
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
        else:
            messages.info(request, 'Sorry, incorrect username or password. Please try again.')
    context = {}
    return render(request, 'login.html', context)

@csrf_exempt
def register_user(request): 

    form = RegisterForm()
   
    if request.method == "POST":
        form = RegisterForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('home:login')

    context = {'form':form}
    return render(request, 'register.html', context)

@csrf_exempt
def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('home:show_home'))
    response.delete_cookie('last_login')
    return response

@csrf_exempt
def edit_profile(request, id):
    # Get product berdasarkan ID
    product = User.objects.get(pk = id)

    # Set product sebagai instance dari form
    form = ChangeForm(request.POST or None, instance=product)

    if form.is_valid() and request.method == "POST":
        # Simpan form dan kembali ke halaman awal
        form.save()
        return HttpResponseRedirect(reverse('user_profile:show_profile'))

    context = {'form': form}
    return render(request, "edit_profile.html", context)

# Create your views here.
@csrf_exempt
def login_flutter(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            # Status login sukses.
            return JsonResponse({
                #"user": serializers.serialize('json', [user,])
                "username": user.username,
                "email": user.email,
                "image_url": user.image_url,
                "id": user.pk,
                "is_superuser": user.is_superuser,
                "status": True,
                "message": "Login sukses!"
                # Tambahkan data lainnya jika ingin mengirim data ke Flutter.
            }, status=200)
        else:
            return JsonResponse({
                "status": False,
                "message": "Login gagal, akun dinonaktifkan."
            }, status=401)

    else:
        return JsonResponse({
            "status": False,
            "message": "Login gagal, periksa kembali email atau kata sandi."
        }, status=401)


@csrf_exempt
def logout_flutter(request):
    username = request.user.username

    try:
        logout(request)
        return JsonResponse({
            "username": username,
            "status": True,
            "message": "Logout berhasil!"
        }, status=200)
    except:
        return JsonResponse({
        "status": False,
        "message": "Logout gagal."
        }, status=401)
    
@csrf_exempt
def register_flutter(request):
    print(f"Request user: {request.user}")
    
    data = json.loads(request.body)
    email = data['username']
    name = data['name']
    passkey = data['password']
    image_url = data['imageUrl']
    
    try:
        user = User.objects.create_user(username=name, password=passkey, email=email, image_url=image_url)
        print("User created")
        return JsonResponse({
            "username": name,
            "status": "success",
            "message": "Pendaftaram akun berhasil!"
        }, status=200)
    except Exception as e:
        # Log the actual exception for debugging purposes
        print(f"Error creating user: {e}")
        return JsonResponse({
            "status": "gagal",
            "message": "Pendaftaran akun gagal."
        }, status=401)
