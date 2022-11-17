from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET'])
def getRoute(requests):
    routes = [
        'GET /api',
        'GET /api/rooms', 
        'GET /api/rooms/:id'
    ]
    # Safe means we can use more the python dictionary inside this form.
    return Response(routes)