from django.shortcuts import render
from django.http import HttpResponse
from scmapp.models import Event
import os

# Create your views here.

def index(request):
    return render(request,'admin_home.html')


#Admin Manage Event Page
def admin_event(request):
    event = Event.objects.all()
    data = {'event':event}

    if 'event_status' in request.session:
        data['status'] = request.session.get('event_status')

    return render(request,'admin_event.html',context=data)

#Admin Update Event Page
def update_event(request,id):
    event = Event.objects.get(eid=id)
    event.date = event.date.strftime('%Y-%m-%d')
    event.time = event.time.strftime('%H:%M:%S')
    data = {'event':event}
    return render(request,'update_event.html',context=data)

#Admin Add Event Page
def add_event(request):
    return render(request,'add_event.html')

#BACKEND -> For Update Event
def db_update_event(request,id):
    if request.method == 'POST':
        event = Event.objects.get(eid=id)
        event.name = request.POST.get('name')
        event.date = request.POST.get('date')
        event.time = request.POST.get('time')
        event.duration = request.POST.get('duration')
        if len(request.FILES) != 0:
            if len(event.image)>0:
                os.remove(event.image.path)
            event.image = request.FILES['image']
        event.save()

        request.session['event_status'] = 'Event updated successfuly'
        return admin_event(request)
    context = {'event':event}
    return render(request,'admin_event.html',context)

#BACKEND -> For Delete Events
def db_delete_event(request,id):
    if request.method == 'GET':
        event = Event.objects.get(eid=id)
        event.delete()

        request.session['event_status'] = 'Event deleted successfuly'
        return admin_event(request)
    else:
        return HttpResponse("Something went wrong!!!!!")

#BACKEND -> For Add Event
def db_add_event(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        date = request.POST.get('date')
        time = request.POST.get('time')
        duration = request.POST.get('duration')
        if len(request.FILES) != 0:
            image = request.FILES['image']

        event = Event(name=name,date=date,time=time,duration=duration,image=image)
        event.save()
        request.session['event_status'] = 'Event added successfuly'
        return admin_event(request)
    else:
        return HttpResponse("Something went wrong!!!!!")
