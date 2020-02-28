from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

from transfer.models import Transfer
from transfer.transfer_serializers.list import TransferListSerializer


class TransferListView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    def get(self, request):
        t_list = Transfer.objects.all()
        serializer = TransferListSerializer(t_list, many=True)
        return Response({"transfers": serializer.data})


