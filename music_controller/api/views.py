from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# Endpoints will be written here; endpoints refer to locations on the server
# Request refers to a client request to the webserver
# A URL needs to point at this function and it will return "Hello!" once pointed
def main(request):
    return HttpResponse("<h1>Hello!</h1>")