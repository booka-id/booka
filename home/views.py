from django.shortcuts import render

def show_home(request):
    
    return render(request, "home.html", context=None)

# Create your views here.
