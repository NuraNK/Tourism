from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from .models import User, Role


class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = (
            'id',
            'name',
        )


class UserRegisterSerializer(serializers.ModelSerializer):
    role = RoleSerializer(read_only=True)

    class Meta:
        model = User
        fields = (
            'id',
            'first_name',
            'last_name',
            'username',
            'email',
            'password',
            'role',
        )

    def validate(self, attrs):
        email = attrs.get('email')
        if User.objects.filter(email=email).exists():
            raise ValidationError("email сущевствует")
        return attrs

    def create(self, validated_data):
        validated_data['is_active'] = True
        validated_data['role'] = Role.objects.get(name='client')
        password = validated_data.get('password')
        user = super().create(validated_data)
        user.set_password(password)
        user.save()

        return user


class ProfileInfoSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'email'
        )
