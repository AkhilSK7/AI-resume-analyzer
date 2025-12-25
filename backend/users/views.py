from django.shortcuts import render
from rest_framework import viewsets
from django.contrib.auth.models import User
from rest_framework.response import Response
from users.serializers import UserSerializer
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status
# Create your views here.

class RegisterAPIView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class LogoutAPIView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self,request):
        try:
            refresh_token=request.data.get('refresh')
            token=RefreshToken(refresh_token)
            token.blacklist()
            return Response({'msg':'Logout successfull'},status=status.HTTP_205_RESET_CONTENT)
        except:
            return Response({'msg':'invalid or expired refresh token'},status=status.HTTP_400_BAD_REQUEST)




