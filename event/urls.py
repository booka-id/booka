from django.urls import path
from django.conf.urls.static import static
from event.views import show_event, create_event, remove_event, edit_event, get_event_json, get_books, create_event_flutter, edit_event_flutter, delete_event_flutter

app_name = 'event'

urlpatterns = [
    path('', show_event, name='show_event'),
    path('create-event/', create_event, name='create_event'),
    path('remove-event/', remove_event, name='remove_event'),
    path('edit-event/<int:id>/', edit_event, name='edit_event'),
    path('edit-event/', edit_event, name='edit_event'),
    path('get-event/', get_event_json, name='get_event_json'),
    path('get-books/', get_books, name='get_books'),
    path('create-event-flutter/', create_event_flutter, name='create_event_flutter'),
    path('edit-event-flutter/<int:id>/', edit_event_flutter, name='edit_event_flutter'),
    path('delete-event-flutter/<int:id>/', delete_event_flutter, name='delete_event_flutter'),
]