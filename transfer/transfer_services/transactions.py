from users.models import User
from django.db import transaction
from currency.models import Currency


def make_transaction(from_user: User, to_user: User, amount):
    if from_user.money < float(amount):
        raise (ValueError('Not Enought money'))
    if from_user == to_user:
        raise (ValueError('Cose another account'))
    with transaction.atomic():
        sender_balance = from_user.money - float(amount)
        from_user.money = sender_balance
        from_user.save()

        sender_currency = from_user.currency
        recipient_currency = to_user.currency
        tr_amount = float(amount)/Currency.objects.get(currency=sender_currency).value
        tr_amount = tr_amount * Currency.objects.get(currency=recipient_currency).value

        recipient_balance = to_user.money + tr_amount
        to_user.money = recipient_balance
        to_user.save()

    return None
