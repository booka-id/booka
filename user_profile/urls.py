from django.urls import path
from user_profile.views import show_profile, add_favorite_book, get_favorite_book

app_name = 'user_profile'

urlpatterns = [
     path('', show_profile, name='show_profile'),
     path('add_favorite_book/', add_favorite_book, name='add_favorite_book'),
     path('get_favorite_book/<str:user_email>/', get_favorite_book, name='get_favorite_book'),

]