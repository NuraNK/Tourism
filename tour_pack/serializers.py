from .models import City, Hotels, Restaurants, Booking
from rest_framework import serializers

class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = (
            'id',
            'city'
        )
class HotelsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotels
        fields = (
            'id',
            'name',
            'city',
            'description',
            'room_num',
            'address',
            'avatarka',
        )


class RestaurantsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurants
        fields = (
            'id',
            'name',
            'city',
            'description',
            'stol_num',
            'address',
            'avatarka',
        )

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = (
            'id',
            'first_name',
            'last_name',
            'restaurant',
            'hotel',
            'reserv_num',
            'phone_number',
            'booking_date',
            'booking_status',
        )