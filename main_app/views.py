from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Finch, Weapon
from .forms import FeedingForm
from django.views.generic import ListView, DetailView

# Create your views here.
# class Finch:  # Note that parens are optional if not inheriting from another class
#   def __init__(self, name, description, diet, beak, habitat):
#     self.name = name
#     self.description = description
#     self.diet = diet
#     self.beak = beak
#     self.habitat = habitat

# tester = [
#   Finch('Small Tree Finch', 'Small Boi with narrow, short beak', 'Insects', 'Grasping Beak', 'in trees'),
#   Finch('Cactus Finch', 'Small Boi with narrow, long beak', 'Cacti', 'Probing Beak', 'on the ground'),
#   Finch('Medium Ground Finch', 'Medium Boi with chonky, short beak', 'Seeds', 'Crushing Beak', 'on the ground'),
#   Finch('Pigeon', 'He got lost', 'Trash', 'Probing Beak', 'Literally Everywhere' )
# ]

def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def finch_index(request):
  finches = Finch.objects.all()
  return render(request, 'finches/index.html', {'finches': finches})

def finch_detail(request, finch_id):
  finch = Finch.objects.get(id=finch_id)
  weapons_finch_doesnt_have = Weapon.objects.exclude(id__in = finch.weapons.all().values_list('id'))
  feeding_form = FeedingForm()
  return render(request, 'finches/detail.html', {
    'finch': finch,
    'feeding_form': feeding_form,
    'weapons': weapons_finch_doesnt_have
  })

def add_feeding(request, finch_id):
  form = FeedingForm(request.POST)
  if form.is_valid():
    new_feeding = form.save(commit=False)
    new_feeding.finch_id = finch_id
    new_feeding.save()
  return redirect('finch-detail', finch_id=finch_id)

def assoc_weapon(request, finch_id, weapon_id):
  Finch.objects.get(id=finch_id).weapons.add(weapon_id)
  return redirect('finch-detail', finch_id=finch_id)

class FinchCreate(CreateView):
  model = Finch
  fields = ['name', 'diet', 'beak', 'habitat', 'description']

class FinchUpdate(UpdateView):
  model = Finch
  fields = ['habitat', 'description']

class FinchDelete(DeleteView):
  model = Finch
  success_url = '/finches/'

class WeaponCreate(CreateView):
  model = Weapon
  fields = '__all__'

class WeaponList(ListView):
  model = Weapon

class WeaponDetail(DetailView):
  model = Weapon

class WeaponUpdate(UpdateView):
  model = Weapon
  fields = ['name', 'color']

class WeaponDelete(DeleteView):
  model = Weapon
  success_url = '/weapons/'