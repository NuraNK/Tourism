from django.shortcuts import render
from rest_framework import generics
from .models import Hotels, RoomsHotel, City, RateHotels, RateRoom
from .serializers import CitySerializer, RoomHotelSerializer, HotelsSerializer, ListHotelsSerializer, RateSerializer, RateRoomSerializer


class CreateHotelView(generics.CreateAPIView):
    serializer_class = HotelsSerializer


class ListHotelView(generics.ListAPIView):
    serializer_class = ListHotelsSerializer
    queryset = Hotels.objects.all()


class CreateRateView(generics.CreateAPIView):
    serializer_class = RateSerializer
    queryset = RateHotels.objects.all()

    def perform_create(self, serializer):
        hotel = self.kwargs['hotel_id']
        user = self.request.user
        serializer.save(author=user, hotel_id=hotel)

    def get_queryset(self):
        return self.queryset.filter(
            hotel_id=self.kwargs['hotel_id']
        )


class CreateRoomView(generics.CreateAPIView):
    serializer_class = RoomHotelSerializer


class CreateRateRoomView(generics.CreateAPIView):
    serializer_class = RateRoomSerializer
    queryset = RateRoom.objects.all()

    def perform_create(self, serializer):
        print(self.kwargs)
        hotel = self.kwargs['hotel_id']
        user = self.request.user
        room = self.kwargs['room_id']
        serializer.save(author=user, hotel_id=hotel, room_id=room)

    def get_queryset(self):
        return self.queryset.filter(
            hotel_id=self.kwargs['hotel_id'],
            room_id=self.kwargs['room_id']
        )


class ListRoomHotelView(generics.ListAPIView):
    serializer_class = RoomHotelSerializer
    queryset = RoomsHotel.objects.all()

    def get_queryset(self):
        return self.queryset.filter(
            hotel_id=self.kwargs['hotel_id'],
            room_id=self.kwargs['room_id']
        )
