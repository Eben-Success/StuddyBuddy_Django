from rest_framework.decorators import api_view
from rest_framework.response import Response
from base.models import Room


@api_view(['GET'])
def getRoute(request):
    routes = [
        'GET /api',
        'GET /api/rooms', 
        'GET /api/rooms/:id'
    ]
    # Safe means we can use more the python dictionary inside this form.
    return Response(routes)

@api_view(['GET'])
def getRooms(request):
    rooms = Room.objects.all()
    return Response(rooms)
    