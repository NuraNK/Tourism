from rest_framework.response import Response

from .models import City, Hotels, Restaurants, Booking
from .serializers import CitySerializer, HotelsSerializer, RestaurantsSerializer, BookingSerializer
from rest_framework.views import APIView
from rest_framework import generics, status


class CityView(generics.CreateAPIView):
    serializer_class = CitySerializer

class HotelsCreateView(generics.CreateAPIView):
    serializer_class = HotelsSerializer

class RestaurantsCreateView(generics.CreateAPIView):
    serializer_class = RestaurantsSerializer

class BookingCreateView(generics.CreateAPIView):
    serializer_class = BookingSerializer

    def post(self, request, *args, **kwargs):
        booking_status = request.data['booking_status']
        print(booking_status)
        if booking_status != "Reserved":
            return Response({"Reserv":"Вы не бронировали Номер"}, status=status.HTTP_400_BAD_REQUEST)
        return self.create(request, *args, **kwargs)

class CancellationReserv(generics.RetrieveUpdateDestroyAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    lookup_field = 'pk'
    def delete(self, request, *args, **kwargs):
        # reserv = self.request['booking_status']
        query = self.queryset.filter(pk=self.kwargs['pk'])
        query.delete()
        return Response(
            {"Delete":"Ваш бронь успешно отменен"},
            status=status.HTTP_200_OK
        )


    def get_queryset(self):
        return self.queryset.filter(pk=self.kwargs['pk'])
