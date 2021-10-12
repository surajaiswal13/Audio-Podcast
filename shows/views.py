# from django.shortcuts import render
from .models import Show
from .serializers import ShowSerializer
from rest_framework.views import APIView
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser

# Create your views here.

class ShowAPIView(APIView):
    permission_classes = [IsAuthenticated, IsAdminUser]

    def get(self, request):
        shows = Show.objects.all()
        serailizer = ShowSerializer(shows, many=True)
        return Response(serailizer.data, status=200)

    def post(self, request):
        data = request.data
        print("1",data)
        serializer = ShowSerializer(data=data)
        print("2",serializer)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

class ShowDetailView(APIView):
    permission_classes = [IsAuthenticated, IsAdminUser]

    def get_object(self, slug):
        try:
            return Show.objects.get(slug=slug)
        except Show.DoesNotExist as e:
            return Response( {"error": "Given Show object not found."}, status=404)

    def get(self, request, slug):
        instance = self.get_object(slug)
        serailizer = ShowSerializer(instance)
        return Response(serailizer.data)

    def put(self, request, slug=None):
        data = request.data
        instance = self.get_object(slug)
        serializer = ShowSerializer(instance, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=400)

    def delete(self, request, slug=None):
        instance = self.get_object(slug)
        instance.delete()
        return HttpResponse(status=204)