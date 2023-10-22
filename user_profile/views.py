from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

@login_required
def show_profile(request):
     context = {
          'user': request.user
     }
     return render(request, 'profile.html', context=context)




# Create your views here.
