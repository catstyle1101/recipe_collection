from django.urls import include, path
from rest_framework import routers

from api.views import IngredientViewSet, RecipeViewSet, TagViewSet
from api.views.users import CustomUserViewSet

app_name = "api"

router_v1 = routers.DefaultRouter()
router_v1.register("recipes", RecipeViewSet)
router_v1.register("ingredients", IngredientViewSet)
router_v1.register("tags", TagViewSet)
router_v1.register("users", CustomUserViewSet, "users")

urlpatterns = [
    path(r"auth/", include("djoser.urls.authtoken")),
    path("", include(router_v1.urls)),
]
