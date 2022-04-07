from django.http import HttpResponse
import datetime

def show(request):
    return HttpResponse("<H1>Hello</H1>")