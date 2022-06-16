from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from rest_framework.response import Response

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


class SignOut(APIView):

    def get(self, request, format=None):
        
        request.user.auth_token.delete()

        return Response({
            'detail': 'User Logged out successfully'
        })