from rest_framework import serializers
from users.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'currency', 'money', 'password')
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
            currency=validated_data['currency'],
            money=validated_data['money'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
class UserTransferSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fileds = ('email',)