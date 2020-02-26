from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework import status

from transfer.models import Transfer
from transfer.transfer_serializers.list import TransferListSerializer
from transfer.transfer_services.find_user import find_user


class TransferListView(APIView):

    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    def get(self, request):
        t_list = Transfer.objects.all()
        serializer = TransferListSerializer(t_list, many=True)
        return Response({"transfers": serializer.data})

    def post(self, request):
        to_user = find_user(request.data.get('to_user'))
        if to_user is None:
            return Response(
                {'error': 'Account "to_user" doesn\'t exist'},
                status=status.HTTP_400_BAD_REQUEST
            )

