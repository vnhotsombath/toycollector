from django.shortcuts import render
from django.http import HttpResponse

class Toy:
    def __init__(self, name, description, world):
        self.name = name
        self.description = description
        self.world = world
toys = [
    Toy('Spider-Man Miles Morales', 'New York teen bitten by a genetically enhanced spider', 'Earth-1610'),
    Toy('Spider-Man Peter Parker', 'New York teen bitten by a genertically enhanced spider', 'Earth-616'),
    Toy('Spider-Man', 'New York teen bitting by a genetically enhanced spider!', 'Earth-1048')

]

# define the home view
def home(request):
    return HttpResponse('<h1>Welcome to the Toy Collector Page!</h1>')

def about(request):
    return render(request, 'about.html')

def toys_index(request):
    return render(request, 'toys/index.html', {'toys': toys})
