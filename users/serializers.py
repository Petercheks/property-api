from rest_framework import serializers

from users.models import User, Rol


class RolSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rol
        fields = '__all__'

    def create(self, validated_data):
        rol = Rol(**validated_data)
        rol.name = (validated_data['name']).upper().replace(" ", "_")
        rol.save()

        return rol

    def update(self, instance, validated_data):
        updated_rol = super().update(instance, validated_data)
        updated_rol.name = (validated_data['name']).upper().replace(" ", "_")
        updated_rol.save()

        return updated_rol



class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'

    def create(self, validated_data):
        user = User(**validated_data)
        user.set_password(validated_data['password'])
        user.save()

        return user

    def update(self, instance, validated_data):
        updated_user = super().update(instance, validated_data)
        updated_user.set_password(validated_data['password'])
        updated_user.save()

        return updated_user


