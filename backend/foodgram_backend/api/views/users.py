from django.db import models
from djoser.views import UserViewSet
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.permissions import DjangoModelPermissions, IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from api.mixins import AddDelViewMixin
from api.pagination import ProjectViewPagination
from api.serializers import UserSubscribeSerializer
from users.models import Subscription, User


class CustomUserViewSet(UserViewSet, ModelViewSet, AddDelViewMixin):
    """
    Viewset for paginated view of User model. implements logic for
    subscriprtion for user by another user. And get list of all subscriptions.
    """
    pagination_class = ProjectViewPagination
    permission_classes = (DjangoModelPermissions,)
    action_serializer = UserSubscribeSerializer

    @action(
        methods=("GET", "POST", "DELETE"),
        detail=True,
        permission_classes=(IsAuthenticated,),
    )
    def subscribe(self, _, id: int | str) -> Response:
        """
        Add or del relation to Subscription model.
        """
        return self.add_del(id, Subscription, models.Q(author__id=id))

    @action(methods=("GET",), detail=False)
    def subscriptions(self, *args) -> Response:
        """
        Get list of current logged user subscriptions.
        """
        if self.request.user.is_anonymous:
            return Response(status=status.HTTP_401_UNAUTHORIZED)

        authors = self.paginate_queryset(
            User.objects.filter(subscribers__user=self.request.user)
        )
        serializer = UserSubscribeSerializer(authors, many=True)
        return self.get_paginated_response(serializer.data)
