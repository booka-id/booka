from django.urls import path
from home.views import show_home, register_user, login_user,logout_user, edit_profile, login_flutter, logout_flutter, register_flutter  

app_name = 'home'

urlpatterns = [
    path('', show_home, name='show_home'),
    path('register/', register_user, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('edit-product/<int:id>', edit_profile, name='edit_profile'),
    path('login_mobile/', login_flutter, name='login_mobile'),
    path('logout_mobile/', logout_flutter, name='logout_mobile'),
    path('register_mobile/', register_flutter, name='register_mobile'),

]