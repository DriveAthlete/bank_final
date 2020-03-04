from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_201_CREATED
)
from transfer.transfer_serializers.TransferCreate import TransferSerializer
from transfer.transfer_services.find_user import find_user
from transfer.transfer_services.transactions import make_transaction

"""
Представление для создания пользователя
"""


class TransferCreateView(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        """

        :param request: to_user: str(email); amount: str(float);
        :return: Responce
        """
        if 'to_user' not in request.data:
            return Response(
                {'error': 'to_user is required'},
                status=HTTP_400_BAD_REQUEST
            )
        """
        Поиск пользлвателя по email
        """
        to_user = find_user(request.data.get('to_user'))
        if to_user is None:
            return Response(
                {'error': 'Account "to_user" doesn\'t exist'},
                status=HTTP_400_BAD_REQUEST
            )
        """
        Транзакция 
        со всеми проверками 
        """
        try:
            make_transaction(from_user=request.user, to_user=to_user, amount=request.data.get('amount'))
        except ValueError as e:
            return Response({'error': str(e)}, status=HTTP_400_BAD_REQUEST)
        """
        Сбор данных для серилезатора
        """
        data = {
            'from_user': request.user.pk,
            'to_user': to_user.pk,
            'amount': request.data.get('amount')
        }
        """
        Серилизация данных 
        """
        serializer = TransferSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(
            status=HTTP_201_CREATED
        )
