from django.shortcuts import render
from django.http import HttpResponse
from django.http import QueryDict
# Create your views here.


def index(req, id):

    return HttpResponse(f'Hello {req.method} {id}')

def id(req):
    a = QueryDict (req.GET.urlencode())
    return HttpResponse(f' {req.GET} { a["sub"] }')
