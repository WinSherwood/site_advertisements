from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Успееееееех")


def test_33(request):
    return HttpResponse('Тест 33')
