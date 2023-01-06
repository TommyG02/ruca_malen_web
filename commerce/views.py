from django.shortcuts import render
from django.http import HttpResponse

def bienvenidos(request):
    return HttpResponse('**** BIENVENIDOS... PROXIMAMENTE... WWW.RUCA-MALEN.COM ****')
