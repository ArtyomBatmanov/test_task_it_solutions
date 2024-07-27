from rest_framework.permissions import AllowAny
from django.contrib.auth import authenticate, login
from .models import Advertisement
from .serializers import AdvertisementSerializer
from mysite import settings
from rest_framework import status
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework import generics, permissions
from rest_framework.views import APIView


class AdvertisementListView(generics.ListAPIView):
    queryset = Advertisement.objects.all().order_by("position")[
        : settings.MAX_POSTS_COUNT
    ]
    serializer_class = AdvertisementSerializer
    permission_classes = [permissions.IsAuthenticated]


class AdvertisementDetailView(generics.RetrieveAPIView):
    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = "id"


class UserRegisterAPIView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")

        if not username or not password:
            return Response(
                {"error": "Username and password are required."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        user = User.objects.create_user(username=username, password=password)

        if user:
            return Response(
                {"message": "User created successfully"}, status=status.HTTP_201_CREATED
            )
        else:
            return Response(
                {"error": "Failed to create user."}, status=status.HTTP_400_BAD_REQUEST
            )


class UserLoginAPIView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")

        if not username or not password:
            return Response(
                {"error": "Username and password are required."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        user = authenticate(username=username, password=password)

        if user:
            login(request, user)
            return Response({"message": "Login successful."}, status=status.HTTP_200_OK)
        else:
            return Response(
                {"error": "Invalid credentials."}, status=status.HTTP_401_UNAUTHORIZED
            )
