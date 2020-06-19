from django.shortcuts import render
from .models import Pokemon, PokemonType
import random

def index(request):
    
    return render(request,'girodm/index.html', context)