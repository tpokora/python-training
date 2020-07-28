from collections import namedtuple

from django.utils.datastructures import MultiValueDictKeyError


def handle_request(request):
    ForecastRequest = namedtuple('ForecastRequest', 'latitude longitude period')
    Period = namedtuple('Period', 'start end')

    req_data = (request.GET['latitude'], request.GET['longitude'],
                Period(none_when_empty(request, 'start'), none_when_empty(request, 'end')))
    req = ForecastRequest._make(req_data)
    return req


def none_when_empty(request, field):
    try:
        value = request.GET[field]
        return value
    except MultiValueDictKeyError:
        return None
