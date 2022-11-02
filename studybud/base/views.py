from django.shortcuts import render

# Create your views here.

rooms = [
    {'id': 1, 'name': "Lets learn python"},
    {'id': 2, 'name': "Design with me"},
    {'id': 3, 'name': "Frontend Developers"},
]

def home(request):
    context = {
        'rooms': rooms
    }
    return render(request, 'base/home.html', context)

# pass pk parameter in room
def room(request, pk):
    return render(request, 'base/room.html')