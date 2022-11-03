from django.shortcuts import render, redirect
from .models import Room, Topic
from .forms import RoomForm
from django.db.models import Q

# Create your views here.

rooms = [
    {'id': 1, 'name': "Lets learn python"},
    {'id': 2, 'name': "Design with me"},
    {'id': 3, 'name': "Frontend Developers"},
]

def home(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    # the i in icontains means insensitive. contains means case sensitive
    rooms = Room.objects.filter(
        Q(topic__name__icontains=q) |
        Q(name__icontains=q) |
        Q(description__icontains=q) 
        )
    
    topics = Topic.objects.all()

    context = {
        'rooms': rooms,
        'topics': topics
    }
    return render(request, 'base/home.html', context)

# pass pk parameter in room
def room(request, pk):
    # id should be unique
    room = Room.objects.get(id=pk)
    return render(request, 'base/room.html')


def createRoom(request):
    form = RoomForm()
    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        

    context = {'form': form}
    return render(request, 'base/room_form.html', context)

def updateRoom(request, pk):
    room = Room.objects.get(id=pk)
    form = RoomForm(instance=room)

    if request.method == 'POST':
        form = RoomForm(request.POST, instance=room)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form': form}
    return render(request, 'base/room_form.html', context)

def deleteRoom(request, pk):
    room = Room.objects.get(id=pk)
    if request.method == 'POST':
        room.delete()
        return redirect('home')
    return render(request, 'base/delete.html', {'obj': room})