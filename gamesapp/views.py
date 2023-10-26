from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from random import randint, choice
from .models import CoinFlip

# Create your views here.


def flip_coin(request):
    result = choice(['Орёл', 'Решка'])
    res = "H" if result == "Орёл" else 'T'
    data = CoinFlip(side=res)
    data.save()
    context = {
        'title': "Орел-решка",
        "result": res,
    }
    return render(request, 'gamesapp/games.html', context=context)


def last_coins(request):
    n = int(request.GET.get('n', '5'))
    print(n)
    data = CoinFlip.get_last_n_stats(n)
    print(data)
    context = {
        'title': "Орел-решка",
        "result": data,
    }
    # return HttpResponse(f'{data}')
    return render(request, 'gamesapp/games.html', context=context)
