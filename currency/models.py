from django.db import models


# Create your models here.
class Currency(models.Model):
    CURRENCY_TYPES = (
        (1, 'EUR'),
        (2, 'USD'),
        (3, 'GPB'),
        (4, 'RUB'),
        (5, 'BTC'),
    )

    currency = models.IntegerField(verbose_name='Currency', choices=CURRENCY_TYPES)
    value = models.FloatField(verbose_name='Value')

    def __str__(self):
        return str(self.currency) + ": " + str(self.value)

    def get_rate(self):
        return {
            'name': self.currency,
            'rate': self.value
        }
