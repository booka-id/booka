import json
from django.shortcuts import render
from event.models import Event
from book.models import Book
from event.forms import EventForm
from django.http import HttpResponseRedirect, HttpResponse, HttpResponseNotFound, JsonResponse
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
from django.contrib.auth.decorators import login_required
from django.utils.dateparse import parse_date

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

@csrf_exempt
def get_books(request):
    books = Book.objects.all()

    return HttpResponse(serializers.serialize('json', books))

def edit_event(request, id=None):
    if (id==None):
        id = request.POST.get('event_id')

    event = Event.objects.get(pk = id)

    form = EventForm(request.POST or None, instance=event)

    if form.is_valid() and request.method == "POST":
        form.save()
        event.featured_book=request.POST.get("featured-book")
        event.save()
        return HttpResponseRedirect(reverse('event:show_event'))

    context = {'form': form, 'event':event}
    return render(request, "edit_event.html", context)
    
@csrf_exempt
def create_event(request):
    if request.method == 'POST':
        name = request.POST.get("name")
        date = request.POST.get("date")
        description = request.POST.get("description")
        photo = request.POST.get("photo")
        featured_book = request.POST.get("featured-book")

        new_event = Event(name=name, date=date, description=description, photo=photo, featured_book=featured_book)
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
def create_event_flutter(request):
    if request.method == 'POST':
        
        data = json.loads(request.body)

        new_event = Event.objects.create(
            name = data["name"],
            featured_book = data["featured_book"],
            date = parse_date(data["date"]),
            description = data["description"],
            photo = data["photo"],
        )

        new_event.save()

        return JsonResponse({"status": "success"}, status=200)
    else:
        return JsonResponse({"status": "error"}, status=401)
    
@csrf_exempt
def edit_event_flutter(request, id):
    try:
        event = Event.objects.get(pk=id)
    except Event.DoesNotExist:
        return JsonResponse({"status": "error", "message": "Event not found"}, status=404)

    if request.method == 'POST':
        data = json.loads(request.body)

        event.name = data.get("name", event.name)
        event.featured_book = data.get("featured_book", event.featured_book)
        event.date = parse_date(data.get("date", str(event.date)))
        event.description = data.get("description", event.description)
        event.photo = data.get("photo", event.photo)

        event.save()

        return JsonResponse({"status": "success"}, status=200)
    else:
        return JsonResponse({"status": "error", "message": "Invalid method"}, status=401)
    
@csrf_exempt
def delete_event_flutter(request, id):
    try:
        event = Event.objects.get(pk=id)
    except Event.DoesNotExist:
        return JsonResponse({"status": "error", "message": "Event not found"}, status=404)

    if request.method == 'DELETE':
        event.delete()
        return JsonResponse({"status": "success"}, status=200)
    else:
        return JsonResponse({"status": "error", "message": "Invalid method"}, status=405)
