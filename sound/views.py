from django.shortcuts import render
from django.http import HttpResponse

from rest_framework.views import APIView

from sound.serializers import LoginSerializer
from django.contrib.auth import login as django_login, logout as django_logout  #We are using this for Session Login 

# For Token Creation and fetching
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication

# Create your views here.

def home(request):
    return HttpResponse("Home Page Test Your APi's With Postman")

class LoginView(APIView):
    def post(self, request):
        print(request.data)
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]
        django_login(request, user)
        token, created = Token.objects.get_or_create(user=user)
        return Response({"token":token.key}, status=200)

class LogoutView(APIView):
    authentication_classes = (TokenAuthentication, )
    def post(self, request):
        # We remove token when logout 
        # because when we use same token we log out from one device it loggs out from every device
        django_logout(request) # removing Token from client side only not from Server side
        return Response(status=204)