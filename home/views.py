from user_profile.forms import RegisterForm, ChangeForm
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages  

def show_home(request):  
    if request.user.is_authenticated:
        user = request.user.username
    else:
        user = 'guest'

    context ={
        'user': user,
    }
    return render(request, "home.html", context=context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home:show_home')
        else:
            messages.info(request, 'Sorry, incorrect username or password. Please try again.')
    context = {}
    return render(request, 'login.html', context)

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

def logout_user(request):
    logout(request)
    return redirect('home:login')


# Create your views here.
