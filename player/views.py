from django.shortcuts import render

# Create your views here.
from player.models import Player
from player.serializers import PlayerSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from player.services import startcheck, check

class PlayerList(APIView):
    """
    List all players, or create a new player.
    """
    def get(self, request, format=None):
        players = Player.objects.all()
        serializer = PlayerSerializer(players, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = PlayerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(wordlist = startcheck(serializer.validated_data["guess"], serializer.validated_data["letterscorrect"]))
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PlayerDetail(APIView):
    
    def get_object(self, pk):
        try:
            return Player.objects.get(pk=pk)
        except Player.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        player = self.get_object(pk)
        serializer = PlayerSerializer(player)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        player = self.get_object(pk)
        currwords = player.wordlist
        serializer = PlayerSerializer(player, data=request.data)
        if serializer.is_valid():
            serializer.save(wordlist = check(serializer.validated_data["guess"], serializer.validated_data["letterscorrect"], currwords))
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        player = self.get_object(pk)
        player.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)