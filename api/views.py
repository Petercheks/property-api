from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from users.serializers import UserSerializer

import datetime


class SignIn(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']

        token, created = Token.objects.get_or_create(user=user)

        user.last_login = datetime.datetime.now()
        user.save()

        return Response({
            'token': token.key,
            'user_id': user.pk,
            'rol_id': user.rol_id,
            'email': user.email,
            'firstname': user.firstname,
            'lastname': user.lastname,
        })


class SignUp(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = UserSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()

        else:
            return Response({'datail': serializer.errors}, status.HTTP_400_BAD_REQUEST)

        sign_in_data = SignIn.post(self, request)

        return sign_in_data


class SignOut(APIView):

    def get(self, request, format=None):
        
        request.user.auth_token.delete()

        return Response({
            'detail': 'User Logged out successfully'
        })