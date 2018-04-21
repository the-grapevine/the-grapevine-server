"""
How to use curl to access the API

curl -X POST -d "username=username&password=password" http://127.0.0.1:8000/api/auth/token/obtain/

This will give us the 2 tokens that we need: refresh and access

We can then use the access token to authenticate with the other views and the refresh token
to get a new access token.

We can then get a list of products by:

curl -X GET -H "Authorization: Bearer <Token>" http://127.0.0.1:8000/api/posts/

"""


from rest_framework import permissions
from rest_framework.generics import CreateAPIView
from django.contrib.auth import get_user_model

from accounts.serializers import UserSerializer

class RegisterView(CreateAPIView):
    model = get_user_model()
    permission_classes = [
        permissions.AllowAny
    ]

    serializer_class = UserSerializer
