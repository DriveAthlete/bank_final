from rest_framework import serializers
from transfer.models import Transfer
from users.serializers import UserSerializer


class TransferListSerializer(serializers.ModelSerializer):
    from_user = UserSerializer()
    to_user = UserSerializer()

    class Meta:
        model = Transfer
        fields = ('from_user', 'to_user', 'amount', 'date')
        # extra_kwargs = {
        #     'from_user': {'read_only': True},
        #     'date': {'read_only': True},
        # }
