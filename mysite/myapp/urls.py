from django.urls import path
from .views import (
    AdvertisementListView,
    AdvertisementDetailView,
    UserRegisterAPIView,
    UserLoginAPIView,
)

urlpatterns = [
    path("advertisements/", AdvertisementListView.as_view(), name="advertisement-list"),
    path(
        "advertisement/<int:id>/",
        AdvertisementDetailView.as_view(),
        name="advertisement-detail",
    ),
    path("register/", UserRegisterAPIView.as_view(), name="user-register"),
    path("login/", UserLoginAPIView.as_view(), name="user-login"),
]
