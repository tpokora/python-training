from collections import namedtuple


def handle_request(request):
    ForecastRequest = namedtuple('ForecastRequest', 'latitude longitude period')
    Period = namedtuple('Period', 'start end')

    req_data = (request.GET['latitude'], request.GET['longitude'],
                Period(none_when_empty(request.GET['start']), none_when_empty(request.GET['end'])))
    req = ForecastRequest._make(req_data)
    return req


def none_when_empty(value):
    if value is None:
        return None
    return value
