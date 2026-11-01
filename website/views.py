from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, JsonResponse
def index_view(request ):
    return HttpResponse('<h1>this is a home page</h1>')


def about_view(request ):
    return HttpResponse('<h1>this is a about view</h1>')

def contact_view(request ):
    return HttpResponse('<h1>this is a contact view</h1>')