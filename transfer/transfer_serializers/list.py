from rest_framework import serializers
from transfer.models import Transfer


class TransferListSerializer(serializers.Serializer):
    class Meta:
        model = Transfer
        fields = ('from_user', 'to_user', 'amount', 'date')
        extra_kwargs = {
            'from_user': {'read_only': True},
            'date': {'read_only': True},
        }

    def create(self, validated_data):
        return Transfer(**validated_data)



