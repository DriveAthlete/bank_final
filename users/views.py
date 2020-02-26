from django.contrib.auth import authenticate
from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from users.serializers import UserSerializer
from rest_framework.authtoken.models import Token


# Create your views here.
class UserCreateView(generics.CreateAPIView):
    serializer_class = UserSerializer
    authentication_classes = ()
    permission_classes = ()


class LoginView(APIView):
    permission_classes = ()

    def post(self, request, ):
        email = request.data.get('email')
        password = request.data.get('password')
        if email is None or password is None:
            return Response({'error': 'Please provide both username and password'},
                            status=status.HTTP_400_BAD_REQUEST)
        user = authenticate(email=email, password=password)
        if not user:
            return Response({'error': 'Invalid Credentials'},
                            status=status.HTTP_404_NOT_FOUND)
        token, _ = Token.objects.get_or_create(user=user)
        return Response({'token': token.key},
                        status=status.HTTP_200_OK)
