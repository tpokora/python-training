from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
from django.template import loader


def index(request):
    message = "Hello World"
    template = loader.get_template('home/index.html')
    context = {
        'msg': message
    }
    return HttpResponse(template.render(context, request))
