from django.urls import path
from home.views import show_home, register_user, login_user,logout_user

app_name = 'home'

urlpatterns = [
    path('', show_home, name='show_home'),
    path('register/', register_user, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),

]