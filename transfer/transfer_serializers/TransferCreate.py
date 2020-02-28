from rest_framework import serializers
from transfer.models import Transfer


class TransferSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transfer
        fields = ('from_user', 'to_user', 'amount', 'date')
