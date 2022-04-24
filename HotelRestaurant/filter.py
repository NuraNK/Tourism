import django_filters
from django.db.models import Q
from django_filters import CharFilter, NumberFilter

from .models import Hotels, RoomsHotel, HotelBooking


class HotelsFilter(django_filters.FilterSet):
    city = django_filters.NumberFilter(field_name='city')
    class Meta:
        model = Hotels
        fields = ['city']

class HotelsRoomFilter(django_filters.FilterSet):
    price_from = django_filters.NumberFilter(field_name='price',
                                            lookup_expr='gte')
    price_to = django_filters.NumberFilter(field_name='price',
                                          lookup_expr='lte')
    from_date = django_filters.DateFilter(field_name='booking_room__date_to',
                                          lookup_expr='gte', exclude=True)
    to_date = django_filters.DateFilter(field_name='booking_room__date_from',
                                        lookup_expr='lte', exclude=True)


    class Meta:
        model = RoomsHotel
        fields = ['num_room']

