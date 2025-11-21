from django.shortcuts import render

# Create your views here.
def index (request):
    return render(request, 'index.html')

def table (request):
    return render(request, 'table.html')

def matches (request):
    return render(request, 'matches.html')

def about (request):
    return render(request, 'about.html')

def auth (request):
    return render(request, 'auth.html')