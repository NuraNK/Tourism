from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.generics import CreateAPIView, RetrieveAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

from .models import User, Role
from .serializers import UserRegisterSerializer, ProfileInfoSerializer


class UserRegisterView(CreateAPIView):
    serializer_class = UserRegisterSerializer
    queryset = User.objects.all()




class CheckEmailPhoneView(APIView):

    def get(self, request):
        email = request.query_params.get('email')

        hasEmail = False

        if User.objects.filter(email=email).exists():
            hasEmail = True

        return Response({"hasEmail": hasEmail})

class LoginView(TokenObtainPairView):
    """ логин для сотрудников """
    serializer_class = TokenObtainPairSerializer

    def post(self, request, *args, **kwargs):
        username = self.request.data.get('username').lower()
        if "@" in username:
            user = User.objects.filter(email=username)
        else:
            user = User.objects.filter(username=username)
        if user:
            user = user.first()
        else:
            return Response({"detail": "Такой пользователь не найден"}, status=status.HTTP_400_BAD_REQUEST)
        role = user.role
        if role:
            roles = []
            for role in Role.objects.all():
                roles.append(role.name)
            if role.name.lower() not in roles:
                return Response({"detail": "вы не являетесть содтрудником"}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"detail": "role net"}, status=status.HTTP_400_BAD_REQUEST)

        return super().post(request, *args, **kwargs)


class ProfileInfoVIew(RetrieveAPIView):
    serializer_class = ProfileInfoSerializer

    def get_object(self):
        user = self.request.user
        return user