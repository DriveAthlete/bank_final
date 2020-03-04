from rest_framework import serializers
from transfer.models import Transfer

"""
Этот серилизатор нужен для предстваления данных для создания
транзакции
"""


class TransferSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transfer
        fields = ('from_user', 'to_user', 'amount', 'date')
