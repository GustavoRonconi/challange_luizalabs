from django.urls import path

from rest_framework_simplejwt import views as jwt_views

from api.views.customer_view import CustomerView

urlpatterns = [
    path("auth/login/", jwt_views.TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("auth/refresh/", jwt_views.TokenRefreshView.as_view(), name="token_refresh",),
    path("customer/", CustomerView.as_view(), name="customer"),
    path("customer/<int:pk>/", CustomerView.as_view(), name="customer"),
]

