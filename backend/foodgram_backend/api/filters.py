from django.db import models
from django_filters import rest_framework as filters
from foodgram.models import Recipe, Tag


class TagFilter(filters.FilterSet):
    name = filters.CharFilter()
    slug = filters.CharFilter()
    color = filters.CharFilter()


class IngredientFilter(filters.FilterSet):

    class Meta:
        model = Tag
        fields = ('name', )

    def name_filter(self, queryset, name, value):
        return queryset.filter(
            models.Q(name__istartswith=value) |
            models.Q(name__icontains=value)
        )


class RecipeFilter(filters.FilterSet):
    name = filters.CharFilter(method='name_filter')
    author = filters.CharFilter(method='author_filter')

    class Meta:
        model = Recipe
        fields = ('name',)

    def name_filter(self, queryset, name, value):
        return queryset.filter(
            models.Q(name__istartswith=value) |
            models.Q(name__icontains=value)
        )

    def author_filter(self, queryset, name, value):
        return queryset.filter(
            models.Q(author__first_name__icontains=value) |
            models.Q(author__first_name__startswith=value) |
            models.Q(author__username__istartswith=value) |
            models.Q(author__username__icontains=value) |
            models.Q(author__last_name__startswith=value) |
            models.Q(author__last_name__icontains=value)
        )
