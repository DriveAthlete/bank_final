from users.models import User
from django.db import transaction


def make_transaction(from_user: User, to_user: User, amount):
    if from_user.money < float(amount):
        raise (ValueError('Not Enought money'))
    if from_user == to_user:
        raise (ValueError('Cose another account'))
    with transaction.atomic():
        sender_balance = from_user.money - float(amount)
        from_user.money = sender_balance
        from_user.save()

        recipient_balance = to_user.money + float(amount)
        to_user.money = recipient_balance
        to_user.save()

    return None
