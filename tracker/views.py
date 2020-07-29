from django.db import models


# Create your views here.
from django.http import HttpResponse


def index(request):
    return HttpResponse("Tracker index page")

