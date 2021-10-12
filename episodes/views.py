# from django.shortcuts import render
from .models import Episode
from shows.models import Show
from .serializers import EpisodeSerializer

from django.http import JsonResponse, HttpResponse
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser


class EpisodeAPIView(APIView):
    permission_classes = [IsAuthenticated, IsAdminUser]

    def get(self, request):
        episodes = Episode.objects.all()
        serailizer = EpisodeSerializer(episodes, many=True)
        return Response(serailizer.data, status=200)

    def post(self, request):
        data = request.data
        print("1",data)
        serializer = EpisodeSerializer(data=data)
        print("2",serializer)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

class EpisodeDetailView(APIView):
    permission_classes = [IsAuthenticated, IsAdminUser]

    def get_object(self, slug):
        try:
            return Episode.objects.get(slug=slug)
        except Episode.DoesNotExist as e:
            return Response( {"error": "Given Episode object not found."}, status=404)

    def get(self, request, slug):
        instance = self.get_object(slug=slug)
        serailizer = EpisodeSerializer(instance)
        return Response(serailizer.data)

    def put(self, request, slug=None):
        data = request.data
        instance = self.get_object(slug)
        serializer = EpisodeSerializer(instance, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=400)

    def delete(self, request, slug=None):
        instance = self.get_object(slug)
        instance.delete()
        return HttpResponse(status=204)

class ViewAllShowEpisodes(APIView):
    permission_classes=[IsAuthenticated, IsAdminUser]

    def get_object(self, slug):
        try:
            print('hello')
            return Show.objects.get(slug=slug)
        except Show.DoesNotExist as e:
            return Response( {"error": "Given Show objects not found."}, status=404)

    def get(self, request, slug):
        show = self.get_object(slug)
        episodes = Episode.objects.filter(show=show.id)
        serailizer = EpisodeSerializer(episodes, many=True)
        return Response(serailizer.data, status=200)
