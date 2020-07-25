# Create your views here.
from django.http import JsonResponse


def home(request):
    return JsonResponse({'message': 'Home'})


def statistic(request):
    longitude = request.GET['longitude']
    latitude = request.GET['latitude']
    response = {
        'message': 'statistic',
        'longitude': longitude,
        'latitude': latitude
    }
    return JsonResponse(response)
