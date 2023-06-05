from django.db.models import Q
from django_filters import rest_framework as filters
from foodgram.models import Recipe, Tag


class IngredientFilter(filters.FilterSet):
    name = filters.CharFilter(lookup_expr='icontains')
# TODO фильтры https://stackoverflow.com/questions/57270470/django-filter-how-to-make-multiple-fields-search-with-django-filter

class RecipeFilter(filters.FilterSet):
    tags = filters.CharFilter(field_name='tags__slug', lookup_expr='exact')