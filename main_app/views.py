from django.shortcuts import render
from django.http import HttpResponse
from .models import Toy


# define the home view
def home(request):
    return HttpResponse('<h1>Welcome to the Toy Collector Page!</h1>')

def about(request):
    return render(request, 'about.html')

def toys_index(request):
    toys = Toy.objects.all()
    return render(request, 'toys/index.html', {'toys': toys})

def toys_detail(request, toy_id):
    toy = Toy.objects.get(id=toy_id)
    return render(request, 'toys/detail.html', { 'toy': toy })
