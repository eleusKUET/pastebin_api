from django.contrib.auth import authenticate
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.views import APIView
from .serializers import CustomUserSerializer, LoginSerializer
from rest_framework.authtoken.models import Token



class LoginView(APIView):
    permission_classes = [permissions.AllowAny]
    authentication_classes = []

    def post(self, request):
        login_serializer = LoginSerializer(data=request.data)
        if login_serializer.is_valid():
            user = authenticate(
                request=request,
                username=login_serializer.validated_data.get('username'),
                password=login_serializer.validated_data.get('password')
            )
            if not user:
                return Response({"detail" : "invalid credentials"}, status=HTTP_400_BAD_REQUEST)

            token, created = Token.objects.get_or_create(user=user)
            return Response({'token' : token.key}, status=HTTP_200_OK)

        return Response(login_serializer.errors, status=HTTP_400_BAD_REQUEST)

class LogoutView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        token = request.auth
        if token:
            token.delete()
            return Response(status=HTTP_200_OK)
        return Response(status=HTTP_400_BAD_REQUEST)


class SignupView(APIView):
    permission_classes = [permissions.AllowAny]
    authentication_classes = []

    def post(self, request):
        signup_serializer = CustomUserSerializer(data=request.data)
        if signup_serializer.is_valid():
            signup_serializer.save()
            return Response(status=HTTP_200_OK)
        return Response(signup_serializer.errors, status=HTTP_400_BAD_REQUEST)

