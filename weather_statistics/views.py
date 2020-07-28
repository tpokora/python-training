# Create your views here.
from django import forms
from django.http import JsonResponse

from weather_statistics.request_handler import handle_request


def home(request):
    return JsonResponse({'message': 'Home'})


class WeatherStatisticsForm(forms.Form):
    latitude = forms.FloatField(required=True)
    longitude = forms.FloatField(required=True)
    start = forms.DateField(input_formats=['%Y-%m-%d'], required=False)
    end = forms.DateField(input_formats=['%Y-%m-%d'], required=False)


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
