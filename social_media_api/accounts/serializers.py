from rest_framework import serializers
from .models import CustomUser
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token


class RegistrationSerialzer(serializers.ModelSerializer):
     class Meta:
        model = CustomUser
        fields = [
            'username', 
            'email', 
            'first_name', 
            'last_name', 
            'password',
        ]

        extra_kwargs = {
            'password': {'write_only': True}
        }

        def create(self, validated_data):
            return CustomUser(**validated_data)
        

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)
    token = serializers.CharField(read_only=True)

    def validate(self, data):
        username = data.get('username')
        password = data.get('password')

        if username and password:
            user = authenticate(username=username, password=password)

            if user:
                token, _ = Token.objects.get_or_create(user=user)
                data['token'] = token.key
            else:
                raise serializers.ValidationError('Unable to log in with provided credentials.')
        else:
            raise serializers.ValidationError('Must include "username" and "password".')

        return data