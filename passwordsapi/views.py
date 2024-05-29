from django.shortcuts import render, HttpResponse
from rest_framework import generics
from .models import UserPassword
from .serializers import UserPasswordSerializer
from rest_framework.permissions import IsAuthenticated
from dotenv import load_dotenv
import os
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from base64 import b64encode,b64decode
# Create your views here.
class CreatePasswordView(generics.ListCreateAPIView):
    serializer_class = UserPasswordSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        currentUser = self.request.user
        return UserPassword.objects.filter(user=currentUser)

    def perform_create(self, serializer):
        if serializer.is_valid():
            pwd = serializer.validated_data["password"].encode('utf-8')
            cipher = AES.new(os.getenv("AES_KEY").encode(),AES.MODE_CBC,iv=os.getenv('NONCE').encode())
            ciphertext = cipher.encrypt(pad(pwd,AES.block_size))
            passwd = b64encode(ciphertext).decode()
            serializer.save(password = passwd,user=self.request.user)
        else:
            print(serializer.errors)


class DeletePasswordView(generics.DestroyAPIView):
    serializer_class = UserPasswordSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return UserPassword.objects.filter(user = self.request.user)
    