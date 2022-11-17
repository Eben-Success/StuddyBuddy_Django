from django.http import JsonResponse

def getRoute(requests):
    routes = [
        'GET /api/rooms', 
        'GET /api/rooms/:id'
    ]
    # Safe means we can use more the python dictionary inside this form.
    return JsonResponse(routes, safe=False)