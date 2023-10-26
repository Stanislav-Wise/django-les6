from django.db import models
from django.utils import timezone
# Create your models here.


class CoinFlip(models.Model):
    SIDE_CHOICES = (
        ('H', 'Heads'),
        ('T', 'Tails'),
    )

    side = models.CharField(max_length=1, choices=SIDE_CHOICES)
    timestamp = models.DateTimeField(default=timezone.now)

    @staticmethod
    def get_last_n_stats(n):
        last_n_stats = CoinFlip.objects.order_by('-timestamp')[:n]
        heads_count = sum(flip.side == 'H' for flip in last_n_stats)
        tails_count = n - heads_count
        return {
            'heads_count': heads_count,
            'tails_count': tails_count,
        }

