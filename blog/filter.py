import django_filters
from django.db.models import Q
from django_filters import CharFilter, NumberFilter

from .models import Blog, Category

class CategoryBlogFilter(django_filters.FilterSet):
    category = NumberFilter(field_name='category')

    class Meta:
        model = Blog
        fields = ['category']