from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.authtoken.models import Token

from api.models import Note



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'is_staff', 'email')
        extra_kwargs = {'password': {
            'write_only': True,
            'required': True
        }}
    def create(self, validated_data):
        usr = User.objects.create_user(**validated_data)
        Token.objects.create(user=usr)
        return usr


class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ('id', 'title', 'body', 'created', 'last_modified')

