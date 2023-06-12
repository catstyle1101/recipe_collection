from django.conf import settings
from rest_framework.pagination import PageNumberPagination


class ProjectViewPagination(PageNumberPagination):
    """
    Pagination to views in project.
    """
    page_size = settings.PAGINATION_COUNT
    page_size_query_param = settings.PAGINATION_QUERY_SIZE_PARAM
    max_page_size = settings.PAGINATION_MAX_COUNT

class ShortRecipeViewPagination(PageNumberPagination):
    """
    Pagination to recipes in sub page.
    """
    page_size = 3
