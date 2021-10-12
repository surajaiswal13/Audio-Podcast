from rest_framework import serializers

from django.contrib.auth import authenticate
from rest_framework import exceptions

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        username = data.get("username", "")
        password = data.get("password", "")
        print(username, password)
        if username and password:
            user = authenticate(username=username, password=password)
            if user:
                if user.is_active:
                    data["user"] = user
                else:
                    msg = "User is InActive or is not Admin"
                    raise exceptions.ValidationError(msg)
            else:
                msg = "Unable to Login with given Credentials"
                raise exceptions.ValidationError(msg)
        else:
            msg = "Must provide Emailid and Password both"
            raise exceptions.ValidationError(msg)
        return data