import django_filters
from django.db.models import Q
from django_filters import CharFilter, NumberFilter

from tour_pack.models import Tour


class TourFilter(django_filters.FilterSet):
    city = django_filters.NumberFilter(field_name='city')
    from_price = django_filters.NumberFilter(field_name='price', lookup_expr='gte')
    to_price = django_filters.NumberFilter(field_name='price', lookup_expr='lte')

    from_date = django_filters.DateFilter(field_name='from_date', lookup_expr='gte')
    to_date = django_filters.DateFilter(field_name='to_date', lookup_expr='lte')
    place = CharFilter(method='search_filter')

    count = NumberFilter(method='search_filter_number')

    class Meta:
        model = Tour
        fields = ['from_date', 'to_date']

    def search_filter(self, queryset, name, value):
        if len(value) > 1:
            queryset = queryset.filter(
                Q(place__name__icontains=value.capitalize())
            ).distinct()

        return queryset

    def search_filter_number(self, queryset, name, value):
        queryset = queryset[:value]

        return queryset
