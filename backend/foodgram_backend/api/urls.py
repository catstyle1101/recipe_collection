from django.urls import include, path
from rest_framework import routers

from api.views import IngredientViewSet, RecipeViewSet, TagViewSet

app_name = "api"

router_v1 = routers.DefaultRouter()
router_v1.register("recipes", RecipeViewSet)
router_v1.register("ingredients", IngredientViewSet)
router_v1.register("tags", TagViewSet)

urlpatterns = [
    path(r"", include("djoser.urls")),
    path(r"auth/", include("djoser.urls.authtoken")),
    path("", include(router_v1.urls)),
]
