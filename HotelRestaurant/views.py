import json

import rest_framework.views
from django.shortcuts import render
import datetime

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework.response import Response

from django.conf import settings
from django.core.mail import send_mail

from base.service import str_to_date, generate_order_book, message
from .filter import HotelsFilter, HotelsRoomFilter
from .models import Hotels, RoomsHotel, City, RateHotels, RateRoom, \
    HotelBooking
from .serializers import CitySerializer, RoomHotelSerializer, HotelsSerializer, \
    ListHotelsSerializer, RateSerializer, \
    RateRoomSerializer, OurRoomsSerializer, BookingSerializer


class CreateHotelView(generics.CreateAPIView):
    serializer_class = HotelsSerializer


class UpdateDestroyHotelView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = HotelsSerializer
    queryset = Hotels.objects.all()


class ListHotelView(generics.ListAPIView):
    serializer_class = ListHotelsSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = HotelsFilter
    queryset = Hotels.objects.all()

    # def get_queryset(self):
    #     queryset = self.queryset.all()
    #     list_of_rating = self.request.query_params.get('ratings', None)
    #     if list_of_rating:
    #         list_of_rating = json.loads(list_of_rating)
    #         queryset = queryset.filter(reviews_hotel__rate__in=list_of_rating)
    #     return queryset


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


class RoomUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = RoomHotelSerializer
    queryset = RoomsHotel.objects.all()

    def get_queryset(self):
        return self.queryset.filter(
            hotel_id=self.kwargs['hotel_id']
        )


class CreateRateRoomView(generics.CreateAPIView):
    serializer_class = RateRoomSerializer
    queryset = RateRoom.objects.all()

    def perform_create(self, serializer):
        hotel = self.kwargs['hotel_id']
        user = self.request.user
        room = self.kwargs['room_id']
        serializer.save(author=user, hotel_id=hotel, room_id=room)

    def get_queryset(self):
        return self.queryset.filter(
            hotel_id=self.kwargs['hotel_id'],
            room_id=self.kwargs['room_id']
        )


class DetailHotelView(generics.ListAPIView):
    serializer_class = HotelsSerializer
    queryset = Hotels.objects.all()

    def get_queryset(self):
        return self.queryset.filter(
            pk=self.kwargs['pk'],
        )


class ListRoomHotelView(generics.ListAPIView):
    serializer_class = RoomHotelSerializer
    queryset = RoomsHotel.objects.all()

    def get_queryset(self):
        return self.queryset.filter(
            hotel_id=self.kwargs['hotel_id'],
            pk=self.kwargs['pk']
        )


class OurRoomsView(generics.ListAPIView):
    serializer_class = OurRoomsSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = HotelsRoomFilter
    queryset = RoomsHotel.objects.all()

    def get_queryset(self):
        queryset = self.queryset.all()
        list_of_rating = self.request.query_params.get('ratings', None)
        if list_of_rating:
            list_of_rating = json.loads(list_of_rating)
            queryset = queryset.filter(reviews_room__rate__in=list_of_rating,
                                       hotel_id=self.kwargs['hotel_id'])

        return queryset


class BookingView(generics.CreateAPIView):
    serializer_class = BookingSerializer
    queryset = HotelBooking.objects.all()

    #
    def post(self, request, *args, **kwargs):
        hotel = self.kwargs['hotel_id'],
        room = self.kwargs['room_id']
        date_from = (request.data.get('date_from'))
        date_to = (request.data.get('date_to'))
        date_to = (str_to_date(date_to))
        date_from = (str_to_date(date_from))
        email = request.data['email']
        # order_num = generate_order_book()
        while True:
            order_num = generate_order_book()
            if not HotelBooking.objects.filter(order_num=order_num):
                break

        if HotelBooking.objects.filter(hotel_id=hotel[0], room_id=room,
                                       date_from=date_from).exists():
            return Response({"error": "error"})
        for i in range((str_to_date(date_to) - str_to_date(date_from)).days):
            HotelBooking.objects.create(
                name=request.data['name'],
                # user=self.request.user,
                email=email,
                order_num=order_num,
                guest=request.data['guest'],
                children=request.data.get("children"),
                hotel_id=hotel[0],
                room_id=room,
                date_from=date_from + datetime.timedelta(i),
                date_to=date_to,
                booking=True
            )
        # send_mail('Вы успешно бронировали номер',
        #           message(order_num, date_from, date_to, room),
        #           settings.EMAIL_HOST_USER,
        #           [email])
        return Response({"detail": "OK"}, status=200)

    def get_queryset(self):
        return self.queryset.filter(
            hotel_id=self.kwargs['hotel_id'],
            room_id=self.kwargs['room_id']
        )


class DeleteBookingView(generics.DestroyAPIView):
    serializer_class = BookingSerializer
    queryset = HotelBooking.objects.all()

    def delete(self, request, *args, **kwargs):
        query = self.queryset.filter(order_num=self.kwargs['order_num'])
        query.delete()
        return Response({"booking": 'Успешно отменили бронь'})

    def get_queryset(self):
        query = self.queryset.filter(
            hotel_id=self.kwargs['hotel_id'],
            room_id=self.kwargs['room_id'],
            order_num=self.kwargs['order_num']
        )
        return query


class IndexHotelView(generics.ListAPIView):
    serializer_class = ListHotelsSerializer
    queryset = Hotels.objects.all()[:5]


class IndexRoomView(generics.ListAPIView):
    serializer_class = OurRoomsSerializer
    queryset = RoomsHotel.objects.all()[:10]
