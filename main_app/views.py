from django.shortcuts import render
from .models import Finch

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
