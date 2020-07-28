from collections import namedtuple


def handle_request(request):
    ForecastRequest = namedtuple('ForecastRequest', 'latitude longitude period')
    Period = namedtuple('Period', 'start end')

    req_data = (float(request.GET.get('latitude')), float(request.GET.get('longitude')),
                Period(request.GET.get('start', None), request.GET.get('end', None)))
    req = ForecastRequest._make(req_data)
    return req


