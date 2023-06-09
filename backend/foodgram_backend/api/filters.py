from django.db import models
from django.db.models import QuerySet, Case, When, Value, IntegerField
from django_filters import rest_framework as filters
from foodgram.models import Recipe, Tag, Ingredient


class TagFilter(filters.FilterSet):
    name = filters.CharFilter()
    slug = filters.CharFilter()
    color = filters.CharFilter()

    class Meta:
        model = Tag
        fields = ("name", "slug", "color")


class IngredientFilter(filters.FilterSet):
    name = filters.CharFilter(method="name_filter")

    class Meta:
        model = Ingredient
        fields = ("name",)

    def name_filter(self, queryset, _, value):
        q1 = models.Q(name__istartswith=value)
        q2 = models.Q(name__icontains=value)
        return queryset.filter(
            q1 | q2
        ).annotate(
            search_ordering=Case(
                When(q1, then=Value(2)),
                When(q2, then=Value(1)),
                default=Value(0),
                output_field=IntegerField(),
            )
        ).order_by('-search_ordering')



class RecipeFilter(filters.FilterSet):
    """
    Filter fo recipes. Uses query params in url.
    """
    name = filters.CharFilter(method="name_filter")
    is_favorited = filters.BooleanFilter(method="in_favorites_filter")
    tags = filters.CharFilter(method="tag_filter")

    class Meta:
        model = Recipe
        fields = ("name", "author")

    def tag_filter(self, queryset: QuerySet, *args) -> QuerySet:
        """
        Filter queryset for tag by slug.
        """
        query_tags = self.request.query_params.getlist("tags")
        tags_subquery = models.Q()
        if query_tags:
            tags_subquery = models.Q(tags__slug__in=query_tags)
        return queryset.filter(tags_subquery).distinct()

    def in_favorites_filter(self, queryset:  QuerySet, *args) -> QuerySet:
        """
        Filter queryset by related in favorites model.
        """
        return queryset.filter(in_favorites__user=self.request.user)

    def name_filter(self, queryset: QuerySet, _, value: str) -> QuerySet:
        """
        Filter queryset by name of tag.
        """
        return queryset.filter(
            models.Q(name__istartswith=value) | models.Q(name__icontains=value)
        )
