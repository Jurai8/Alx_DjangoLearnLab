from django.shortcuts import render
from rest_framework.views import APIView
from .models import CustomUser
from .serializers import RegistrationSerialzer, LoginSerializer
from rest_framework.response import Response


# Create your views here.

class RegistrationView(APIView):
    serializer_class = [RegistrationSerialzer]
    permission_classes = [] #

    pass


class LoginView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data)