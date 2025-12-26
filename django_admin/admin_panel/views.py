from django.http import JsonResponse
from .models import Student


def index(request):
    data = list(
        Student.objects.values()
    )
    return JsonResponse({
        'status': True,
        'message': 'success',
        'data': data
    })
