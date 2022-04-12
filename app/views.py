from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

# Create your views here.
def send_the_homepage(request):
    theIndex = open('build/index.html').read()
    print(theIndex)
    return HttpResponse(theIndex)