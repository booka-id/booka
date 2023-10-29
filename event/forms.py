from django.forms import ModelForm
from event.models import Event

class EventForm(ModelForm):
    class Meta:
        model = Event
        fields = ["name", "date", "description", "photo"]