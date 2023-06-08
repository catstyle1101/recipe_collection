from django.db import models
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
        return queryset.filter(
            models.Q(name__istartswith=value) | models.Q(name__icontains=value)
        )


class RecipeFilter(filters.FilterSet):
    name = filters.CharFilter(method="name_filter")
    is_favorited = filters.BooleanFilter(method="in_favorites_filter")
    tags = filters.CharFilter(method="tag_filter")

    class Meta:
        model = Recipe
        fields = ("name", "author")

    def tag_filter(self, queryset, _, value):
        query_tags = self.request.query_params.getlist("tags")
        tags_subquery = models.Q()
        if query_tags:
            tags_subquery = models.Q(tags__slug__in=query_tags)
        return queryset.filter(tags_subquery).distinct()

    def in_favorites_filter(self, queryset, *args):
        return queryset.filter(in_favorites__user=self.request.user)

    def name_filter(self, queryset, _, value):
        return queryset.filter(
            models.Q(name__istartswith=value) | models.Q(name__icontains=value)
        )
