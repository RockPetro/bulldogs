from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, redirect
from .models import Player

# Create your views here.

def playerRoster(request):
    players = Player.objects.all()
    search_input = request.GET.get('search-area')
    if search_input:
        players = Player.objects.filter(jersey__icontains=search_input)
    else:
        players = Player.objects.all()
        search_input = ''
    return render(request, 'roster.html', {'players': players, 'search_input': search_input})


def playerProfile(request, jersey):
    player = Player.objects.get(jersey=jersey)
    return render(request, 'player-profile.html', {'player':player})