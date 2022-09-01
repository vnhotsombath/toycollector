from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Toy, Ability
from .forms import PieceForm, AbilityForm

# define the home view
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def toys_index(request):
    toys = Toy.objects.all()
    return render(request, 'toys/index.html', {'toys': toys})

def toys_detail(request, toy_id):
    toy = Toy.objects.get(id=toy_id)
    piece_form = PieceForm()
  
    return render(request, 'toys/detail.html', { 'toy': toy, 'piece_form': piece_form })

def add_piece(request, toy_id):
    form = PieceForm(request.POST)
    if form.is_valid():
        new_piece = form.save(commit=False)
        new_piece.toy_id = toy_id
        new_piece.save()
    return redirect('detail', toy_id=toy_id)

def add_ability(request, toy_id):
    form = AbilityForm(request.POST)
    if form.is_valid():
        new_ability = form.save(commit=False)
        new_ability = toy_id = toy_id
        new_ability.save()
    return redirect('detail', toy_id=toy_id)

class AbilityList(ListView):
    model = Ability

class AbilityDetail(DetailView):
    model = Ability 

class AbilityCreate(CreateView):
    model = Ability
    fields = '__all__'

class AbilityUpdate(UpdateView):
    model = Ability
    fields = ['description']

class AbilityDelete(DeleteView):
    model = Ability
    success_url = '/toys/'

class ToyCreate(CreateView):
    model = Toy
    fields = '__all__'

class ToyUpdate(UpdateView):
    model = Toy
    fields = ['description', 'age']

class ToyDelete(DeleteView):
    model = Toy
    success_url = '/toys/'