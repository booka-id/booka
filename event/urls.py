from django.urls import path
from django.conf.urls.static import static
from event.views import show_event, create_event, remove_event, edit_event, get_event_json, register_event, get_books

app_name = 'event'

urlpatterns = [
    path('', show_event, name='show_event'),
    path('create-event/', create_event, name='create_event'),
    path('remove-event/', remove_event, name='remove_event'),
    path('edit-event/<int:id>/', edit_event, name='edit_event'),
    path('edit-event/', edit_event, name='edit_event'),
    path('register-event/<int:event_id>/', register_event, name='register_event'),
    path('get-event/', get_event_json, name='get_event_json'),
    path('get-books/', get_books, name='get_books'),
]