from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
class Finch:  # Note that parens are optional if not inheriting from another class
  def __init__(self, name, description, diet, beak, habitat):
    self.name = name
    self.description = description
    self.diet = diet
    self.beak = beak
    self.habitat = habitat

tester = [
  Finch('Small Tree Finch', 'Small Boi with narrow, short beak', 'Insects', 'Grasping Beak', 'in trees'),
  Finch('Cactus Finch', 'Small Boi with narrow, long beak', 'Cacti', 'Probing Beak', 'on the ground'),
  Finch('Medium Ground Finch', 'Medium Boi with chonky, short beak', 'Seeds', 'Crushing Beak', 'on the ground'),
  Finch('Pigeon', 'He got lost', 'Trash', 'Probing Beak', 'Literally Everywhere' )
]

def home(request):
  return HttpResponse('<h1>Hello ᓚᘏᗢ</h1>')

def about(request):
  return render(request, 'about.html')

def finch_index(request):
  return render(request, 'finches/index.html', {'finches': tester})