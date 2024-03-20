from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token



def register_page(request):
    return render(request, "accounts/register.html")

def login_page(request):
    return render(request, "accounts/login.html")


class RegisterUserAPIView(APIView):
    def post(self, request, *args, **kwargs):
        username = request.data.get('username')
        password = request.data.get('password')
        password2 = request.data.get('password2')

        if password != password2:
            return Response({'error': 'Password incorrect'}, status=status.HTTP_400_BAD_REQUEST)

        if User.objects.filter(username=username).exists():
            return Response({'error': 'Username already exists.'}, status=status.HTTP_400_BAD_REQUEST)

        user = User.objects.create_user(username=username, password=password)
        token, created = Token.objects.get_or_create(user=user)

        return Response({'token': token.key}, status=status.HTTP_201_CREATED)
    

# class LoginUserAPIView(APIView):
#     def post(self, request, *args, **kwargs):
#         username = request.data.get('username')
#         password = request.data.get('password')
#         user = authenticate(username=username, password=password)

#         if user is None:
#             return Response({'error': 'User not found'}, status=status.HTTP_400_BAD_REQUEST)
        
#         token, created = Token.objects.get_or_create(user=user)
#         return Response({'token': token.key}, status=status.HTTP_201_CREATED)
    

class LogoutUserAPIView(APIView):
    def get(self, request):
        user_token = Token.objects.get(user=1)    # request.user
        if user_token is None:
            return Response({'error': 'Token not found'}, status=status.HTTP_400_BAD_REQUEST)
        
        user_token.delete()
        return Response({'success': f"{user_token.user.username} token deleted!"})
        




