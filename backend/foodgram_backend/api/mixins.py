from typing import Type, TypeVar

from django.db import models
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response

Model = TypeVar('Model', bound=models.Model)

class AddDelViewMixin:
    """
    Implements logic to add or delete m2m relation with model.
    Uses action_serialiser for serialize data in response.
    """
    action_serializer = None

    def add_del(
        self: Request,
        id: int | str,
        model: Type[Model],
        query_to_join: models.Q,
    ) -> Response:
        """
        add or del relation in model using query_to_join and id key.
        """
        obj = get_object_or_404(self.queryset, id=id)
        serialized_data = self.action_serializer(obj)
        joined_data_query = model.objects.filter(
            query_to_join & models.Q(user=self.request.user)
        )

        if self.request.method in ("GET", "POST") and not joined_data_query:
            model(None, id, self.request.user.id).save()
            return Response(
                serialized_data.data, status=status.HTTP_201_CREATED
            )
        if self.request.method == "DELETE" and joined_data_query:
            joined_data_query[0].delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_400_BAD_REQUEST)
