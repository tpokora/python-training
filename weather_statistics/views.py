# Create your views here.
from django.http import JsonResponse

from weather_statistics.request_handler import handle_request


def home(request):
    return JsonResponse({'message': 'Home'})


def statistic(request):

    # TODO: Validate request
    req = handle_request(request)

    response = {
        'message': 'statistic',
        'longitude': req.longitude,
        'latitude': req.latitude,
        'from': req.period.start,
        'to': req.period.end
    }
    return JsonResponse(response)
