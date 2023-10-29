from django.urls import path
from user_profile.views import show_profile, add_favorite_book, get_favorite_book, get_wishlist, add_wishlist, get_user_by_username, user_profile_page

app_name = 'user_profile'

urlpatterns = [
     path('', show_profile, name='show_profile'),
     path('add_favorite_book/', add_favorite_book, name='add_favorite_book'),
     path('get_favorite_book/<str:user_email>/', get_favorite_book, name='get_favorite_book'),
     path('add_wishlist/', add_wishlist, name='add_wishlist'),
     path('get_wishlist/<str:user_email>/', get_wishlist, name='get_wishlist'),
     path('user_by_username/', get_user_by_username, name='user_by_username'),
     path('go_to/<str:username>/', user_profile_page, name='go_to_user_profile'),
     

]