# views.py
from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import LoginSerializer
from rest_framework import status, generics
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import LoginSerializer
from django.core.mail import send_mail
from .serializers import (
    RegistrationSerializer, LoginSerializer, 
    LogoutSerializer,ChangePasswordSerializer, ResetPasswordSerializer
)
from apps.custom_user.models import User



class UserRegistrationView(generics.GenericAPIView):
    serializer_class = RegistrationSerializer
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(
            {"message": "User registered successfully. Please proceed to login."},
            status=status.HTTP_201_CREATED
        )



class LoginUserView(generics.GenericAPIView):
    serializer_class = LoginSerializer
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        user = serializer.validated_data.get('user')
        refresh = RefreshToken.for_user(user)
        access_token = str(refresh.access_token)
        refresh_token = str(refresh)

        # Generate response and set tokens as cookies
        response = Response(
            {
                "message": "Login successful",
            },
            status=status.HTTP_200_OK
        )

        # Set the tokens as HTTP-only cookies for security
        response.set_cookie(
            'access_token',
            access_token,
            httponly=True,
            secure=True,  # Set to True when using HTTPS
            samesite='Lax'
        )
        response.set_cookie(
            'refresh_token',
            refresh_token,
            httponly=True,
            secure=True,  # Set to True when using HTTPS
            samesite='Lax'
        )

        return response




class LogoutView(generics.GenericAPIView):
    serializer_class = LogoutSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        try:
            refresh_token = serializer.validated_data['refresh']
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(
                {"message": "Logout successful"},
                status=status.HTTP_200_OK
            )
        except Exception as e:
            return Response(
                {"error": "Logout failed", "details": str(e)},
                status=status.HTTP_400_BAD_REQUEST
            )



class ChangePasswordView(generics.GenericAPIView):
    serializer_class = ChangePasswordSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = request.user
        if not user.check_password(serializer.validated_data['old_password']):
            return Response({"error": "Old password is incorrect"}, status=status.HTTP_400_BAD_REQUEST)

        user.set_password(serializer.validated_data['new_password'])
        user.save()
        return Response({"message": "Password updated successfully"}, status=status.HTTP_200_OK)



class ResetPasswordView(generics.GenericAPIView):
    serializer_class = ResetPasswordSerializer

    def post(self, request, *args, **kwargs):
        # sourcery skip: use-named-expression
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        email = serializer.validated_data['email']
        user = User.objects.filter(email=email).first()

        if user:
            # Simulate password reset email
            reset_link = "http://example.com/reset-password/"
            send_mail(
                subject="Password Reset Request",
                message=f"Use this link to reset your password: {reset_link}",
                from_email="kakdepatil333@gmail.com",
                recipient_list=[email],
            )
            return Response({"message": "Password reset email sent"}, status=status.HTTP_200_OK)
        
        return Response({"error": "User with this email not found"}, status=status.HTTP_400_BAD_REQUEST)



class UserCountView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user_count = User.objects.count()
        return Response({"user_count": user_count}, status=status.HTTP_200_OK)
