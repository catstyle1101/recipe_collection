from django.urls import include, path
from rest_framework import routers

app_name = "api"

router_v1 = routers.DefaultRouter()

urlpatterns = [
    path(r"", include("djoser.urls")),
    path(r"auth/", include("djoser.urls.authtoken")),
    path("", include(router_v1.urls)),
]
