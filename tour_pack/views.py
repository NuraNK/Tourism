from datetime import datetime

from django.db.models import Q, Sum
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from rest_framework.generics import ListAPIView, RetrieveAPIView, ListCreateAPIView
from rest_framework.views import APIView

from HotelRestaurant.models import City
from tour_pack.filter import TourFilter
from tour_pack.models import Tour, TourOrder
from tour_pack.serializers import ListTourSerializer, CitySerializer, ListTourSingleSerializer, TourOrderSerializer


class ListTourView(ListAPIView):
    serializer_class = ListTourSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = TourFilter
    queryset = Tour.objects.all()

    def get_queryset(self):
        queryset = self.queryset.filter(from_date__gt=datetime.now().date())

        return queryset


class RetrieveListTourView(RetrieveAPIView):
    serializer_class = ListTourSingleSerializer
    queryset = Tour.objects.all()
    lookup_field = 'pk'


class ListCityView(ListAPIView):
    serializer_class = CitySerializer
    queryset = City.objects.all()


class CheckPlaceView(APIView):

    def post(self, request, pk, *args, **kwargs):
        count = request.data.get("count")
        tour = Tour.objects.get(pk=pk)
        if not tour or count is None:
            return Response(
                {
                    "msg": "Pk or count is invalid",
                    "status": False
                }
            )

        all_count = tour.count

        if TourOrder.objects.filter(user=request.user, tour=tour):
            return Response({
                "msg": "Вы уже забронировали мест",
                "status": False
            })

        order_count = TourOrder.objects.filter(tour=tour, confirm=True).aggregate(Sum('count')).get("count__sum")

        if order_count:
            if all_count - (order_count + count) >= 0:
                return Response({
                    "msg": "Мест есть",
                    "status": True
                })
        else:
            if all_count - count >= 0:
                return Response({
                    "msg": "Мест есть",
                    "status": True
                })

        return Response({
            "msg": "Нет мест",
            "status": False
        })


class TourOrderList(ListCreateAPIView):
    queryset = TourOrder.objects.all()
    serializer_class = TourOrderSerializer

    def perform_create(self, serializer):
        print(self.request.user)
        serializer.save(user=self.request.user)
