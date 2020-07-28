# Create your views here.
from django.http import JsonResponse

from weather_statistics.forms import WeatherStatisticsForm
from weather_statistics.request_handler import handle_request


def home(request):
    return JsonResponse({'message': 'Home'})


def statistic(request):
    weather_form = WeatherStatisticsForm(request.GET)

    if not weather_form.is_valid():
        return JsonResponse({'error': 'invalid form'}, status=400)

    req = handle_request(request)

    response = {
        'message': 'statistic',
        'longitude': req.longitude,
        'latitude': req.latitude,
        'from': req.period.start,
        'to': req.period.end
    }
    return JsonResponse(response)
