from django.shortcuts import render, redirect
from .models import Room
from .forms import RoomForm

# Create your views here.

rooms = [
    {'id': 1, 'name': "Lets learn python"},
    {'id': 2, 'name': "Design with me"},
    {'id': 3, 'name': "Frontend Developers"},
]

def home(request):
    rooms = Room.objects.all()
    context = {
        'rooms': rooms
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
        

    context = {'form': form}
    return render(request, 'base/room_form.html', context)