from django.urls import path, include

from rest_framework_simplejwt import views as jwt_views
from rest_framework import routers

from api.views.customer_view import CustomerView


router = routers.DefaultRouter()
router.register(r"customer", CustomerView, basename="customer")


urlpatterns = [
    path("auth/login/", jwt_views.TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("auth/refresh/", jwt_views.TokenRefreshView.as_view(), name="token_refresh",),
    path("", include(router.urls)),
]

