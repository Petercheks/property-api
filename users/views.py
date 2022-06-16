from django.shortcuts import get_object_or_404

from rest_framework import viewsets, status
from rest_framework.response import Response

from users.serializers import UserSerializer, RolSerializer
from users.models import User, Rol


class UserViewSet(viewsets.ViewSet):

    queryset = User.objects.all()
    
    def list(self, request):
        query = User.objects.all()
        serializer = UserSerializer(query, many=True)

        return Response(serializer.data, status.HTTP_200_OK)    

    def retrieve(self, request, pk):
        query = User.objects.all()
        user = get_object_or_404(query, pk=pk)
        serializer = UserSerializer(user)
        
        return Response(serializer.data, status.HTTP_200_OK)

    def create(self, request):
        user = UserSerializer(data=request.data)
        
        if user.is_valid():
            user.save()
        else:
            return Response({'datail': user.errors}, status.HTTP_400_BAD_REQUEST)

        return Response(user.data, status.HTTP_201_CREATED)

    def update(self, request, pk=None):
        user = get_object_or_404(User, pk=pk)
        serializer = UserSerializer(instance=user, data=request.data)

        if serializer.is_valid():
            serializer.save()
        else:
            return Response({'datail': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

        return Response(serializer.data, status.HTTP_200_OK)

    def destroy(self, request, pk=None):
        user = get_object_or_404(User, pk=pk)
        user.delete()

        return Response(UserSerializer(user).data, status.HTTP_200_OK)


class RolViewSet(viewsets.ViewSet):

    queryset = Rol.objects.all()
    
    def list(self, request):
        query = Rol.objects.all()
        serializer = RolSerializer(query, many=True)

        return Response(serializer.data, status.HTTP_200_OK)  

    def create(self, request):
        rol = RolSerializer(data=request.data)

        if rol.is_valid():
            rol.save() 
        else:
            return Response({'datail': rol.errors}, status.HTTP_400_BAD_REQUEST)

        return Response(rol.data, status.HTTP_201_CREATED)

    def update(self, request, pk=None):
        rol = get_object_or_404(Rol, pk=pk)
        serializer = RolSerializer(instance=rol, data=request.data)

        if serializer.is_valid():
            serializer.save()
        else:
            return Response({'datail': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

        return Response(serializer.data, status.HTTP_200_OK)

    def destroy(self, request, pk=None):
        rol = get_object_or_404(Rol, pk=pk)
        rol.delete()

        return Response(RolSerializer(rol).data, status.HTTP_200_OK)