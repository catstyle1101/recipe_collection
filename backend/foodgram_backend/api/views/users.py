from djoser.views import UserViewSet
from rest_framework.viewsets import ModelViewSet

from api.pagination import ProjectViewPagination


class CustomUserViewSet(UserViewSet, ModelViewSet):
    pagination_class = ProjectViewPagination