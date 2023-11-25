from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from .models import *


class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = ('id', 'name', 'birthdate', 'gender')

        def validate_birthdaet(self, value):
            if value < '01.01.1950':
                raise ValidationError(
                    detail='01.01.1950 dan katta sanani kiriting!!!'
                )
            return value


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
