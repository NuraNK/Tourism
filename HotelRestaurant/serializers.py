from rest_framework import serializers

from accounts.models import User
from .models import City, Hotels, RoomsHotel, ReviewTotal, RateHotels, RateRoom


class ReviewTotalSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReviewTotal
        fields = ('rate', 'total')

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id',
            'email',
        )

class RateSerializer(serializers.ModelSerializer):
    class Meta:
        model = RateHotels
        fields = (
            'id',
            'rate',
        )

class RateRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = RateRoom
        fields = (
            'id',
            'rate',
        )

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
            'avatar_hotel',
            'photo_hotel',
            'adress',
        )


class ListHotelsSerializer(serializers.ModelSerializer):
    reviews_hotel = serializers.SerializerMethodField()
    class Meta:
        model = Hotels
        fields = (
            'id',
            'name',
            'city',
            'reviews_hotel',
            'description',
            'avatar_hotel',
        )
    def get_reviews_hotel(self, obj):
        return ReviewTotalSerializer(obj.hotel_totals.all().first()).data

class RoomHotelSerializer(serializers.ModelSerializer):
    reviews_room = serializers.SerializerMethodField()

    class Meta:
        model = RoomsHotel
        fields = (
            'id',
            'hotel',
            'num_room',
            'description',
            'price',
            'avatar_room',
            'photo_room',
            'reviews_room'
        )

    def get_reviews_room(self, obj):
        return ReviewTotalSerializer(obj.room_totals.all().first()).data

