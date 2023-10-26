from django.urls import path
from .views import flip_coin, last_coins

urlpatterns = [
    path('coin/', flip_coin, name='coin'),
    path('last_coins/', last_coins, name='last_coins'),
]
