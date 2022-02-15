from wsgiref import validate
from django.db import models
from rest_framework import serializers
from setuptools import Require
from player.models import Player

class PlayerSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    guess = serializers.CharField(max_length = 5)
    letterscorrect = serializers.CharField(max_length = 5)
    win = serializers.BooleanField(default = False)
    wordlist = serializers.ListField(read_only = True)

    def create(self, validated_data):
        return Player.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.guess = validated_data.get('guess', instance.guess)
        instance.letterscorrect = validated_data.get('letterscorrect', instance.letterscorrect)
        instance.win = validated_data.get('win', instance.win)
        instance.wordlist = validated_data.get('wordlist', instance.wordlist)
        instance.save()
        return instance

