from django.db import models


# Create your models here.
class Currency(models.Model):
    name = models.CharField(max_length=6)
    rate = models.FloatField()

    def __str__(self):
        return str(self.name) + ": " + str(self.rate)

    def get_rate(self):
        return {
            'name': self.name,
            'rate': self.rate
        }
