from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)


# Create your transfer_models here.

class User(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='Email',
        max_length=255,
        unique=True,
        db_index=True,
    )
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['currency', 'money']
    CURRENCY_TYPES = (
        (1, 'EUR'),
        (2, 'USD'),
        (3, 'GPB'),
        (4, 'RUB'),
        (5, 'BTC'),
    )
    currency = models.IntegerField(verbose_name='Currency', choices=CURRENCY_TYPES)
    money = models.IntegerField(verbose_name='Money')

    objects = BaseUserManager()

    def __str__(self):
        return self.email
