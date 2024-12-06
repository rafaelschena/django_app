from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(response):
    return HttpResponse('<h1>PdM Dashboard</h1>')

def history(response):
    return HttpResponse('<h1>History</h1>')