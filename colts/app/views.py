from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index (request):
    return render(request, 'indsex.html')

def table (request):
    return render(request, 'table.html')

def matches (request):
    return render(request, 'matches.html')

def about (request):
    return render(request, 'about.html')