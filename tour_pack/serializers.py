from rest_framework import serializers

from HotelRestaurant.models import City
from tour_pack.models import Tour, Place, Gallery, TourOrder


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = "__all__"


class PlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Place
        fields = ('id', 'name',)


class GallerySerializer(serializers.ModelSerializer):
    class Meta:
        model = Gallery
        fields = ('id', 'image',)


class ListTourSerializer(serializers.ModelSerializer):
    city = CitySerializer(read_only=True)
    place = PlaceSerializer(many=True, read_only=True)

    class Meta:
        model = Tour
        fields = (
            'id',
            'name',
            'image',
            'price',
            'count',
            'duration_text',
            'city',
            'place',
            'from_date',
            'to_date',
            'short_description',
        )


class ListTourSingleSerializer(serializers.ModelSerializer):
    city = CitySerializer(read_only=True)
    place = PlaceSerializer(many=True, read_only=True)
    gallery = GallerySerializer(many=True, read_only=True)
    description = serializers.SerializerMethodField()

    class Meta:
        model = Tour
        fields = "__all__"

    def get_description(self, obj):
        desc = obj.description.html
        return desc


class TourOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = TourOrder
        exclude = ('user', )
