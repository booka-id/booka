from django.shortcuts import render
from event.models import Event
from event.forms import EventForm
from django.http import HttpResponseRedirect, HttpResponse, HttpResponseNotFound
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers

def show_event(request):
    events = Event.objects.all()

    context = {
        'events' : events,
        'user' : request.user,
    }

    return render(request, "event.html", context)

def get_event_json(request):
    event_item = Event.objects.all()
    return HttpResponse(serializers.serialize('json', event_item))

def edit_event(request, id=None):
    if (id==None):
        id = request.POST.get('event_id')

    event = Event.objects.get(pk = id)

    form = EventForm(request.POST or None, instance=event)

    if form.is_valid() and request.method == "POST":
        form.save()
        return HttpResponseRedirect(reverse("event:show_event"))

    context = {'form': form, 'event':event}
    return render(request, "edit_event.html", context)
    

@csrf_exempt
def create_event(request):
    if request.method == 'POST':
        name = request.POST.get("name")
        date = request.POST.get("date")
        description = request.POST.get("description")

        new_event = Event(name=name, date=date, description=description)
        new_event.save()

        return HttpResponse(b"CREATED", status=201)

    return HttpResponseNotFound()

@csrf_exempt
def remove_event(request):
    if request.method == 'POST':
        id=request.POST.get("id")
        event = Event.objects.get(pk=id)
        event.delete()
        response = HttpResponse(status=200)
        return response
    return HttpResponseNotFound()

@csrf_exempt
def register_event(request, id):
     return render(request, 'register_event.html', {'id':id})