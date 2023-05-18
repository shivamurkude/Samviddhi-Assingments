from rest_framework.views import APIView
from rest_framework.response import Response

from django.contrib.auth import authenticate
from .serializer import RegistrationSerializer,UserSerializer
from rest_framework.permissions import AllowAny
from rest_framework import status
from django.contrib.auth import get_user_model
import traceback

User = get_user_model()


class UserView(APIView):
    permission_classes = (AllowAny,)
    def post(self, request):
        try:
            serializer = RegistrationSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            traceback.print_exc()

    def get(self, request):
        try:

            users = User.objects.all()
            if not users:
                return Response("No users",status=status.HTTP_204_NO_CONTENT)
            
            serializer = UserSerializer(users, many=True)
            return Response(serializer.data)
        except Exception as e:
            traceback.print_exc()