# from rest_framework.response import Response
# from datetime import date, timedelta
#
# from base.service import str_to_date
# from .models import City, Hotels, Restaurants, BookingHotel
# from .serializers import CitySerializer, HotelsSerializer, RestaurantsSerializer, BookingHotelSerializer, \
#     BookingRestaurantSerializer
# from rest_framework.views import APIView
# from rest_framework import generics, status
#
#
# class CityView(generics.CreateAPIView):
#     serializer_class = CitySerializer
#
#
# class HotelsCreateView(generics.CreateAPIView):
#     serializer_class = HotelsSerializer
#
#
# class RestaurantsCreateView(generics.CreateAPIView):
#     serializer_class = RestaurantsSerializer
#
#
# class BookingHotelCreateView(generics.CreateAPIView):
#     serializer_class = BookingHotelSerializer
#
#     def post(self, request, *args, **kwargs):
#         booking_status = request.data['booking_status']
#         # print(booking_status)
#
#         bd_from = request.data['booking_date_from']
#         reserv_num = request.data['reserv_num']
#         bd_to = request.data['booking_date_to']
#
#         # print(type(bd_to), bd_from)
#
#         bd = str_to_date(bd_to) - str_to_date(bd_from)
#         bd_res = []
#         for i in range(1, bd.days):
#             bd_res.append(
#                 str_to_date(bd_from) + timedelta(days=i + 1)
#             )
#         # print(bd_res)
#         object_date = BookingHotel.objects.filter(reserv_num_id=int(reserv_num))
#         # print(object_date)
#         bd_check_res = []
#         obj_d = object_date[len(object_date) - 1]
#         # print(obj_d.__dir__())
#         bd_chech_date_from = obj_d.booking_date_from
#         bd_chech_date_to = obj_d.booking_date_to
#         bd_chech_date = (bd_chech_date_to) - (bd_chech_date_from)
#
#         for i in range(1, bd_chech_date.days):
#             bd_check_res.append(
#                 bd_chech_date_from + timedelta(days=i + 1)
#             )
#         # print(bd_res, bd_check_res)
#
#         for i in bd_res:
#             if i in bd_check_res:
#                 return Response({'detail': f'{bd_check_res[0]} - {bd_check_res[-1]}  уже бронирован'}, status=status.HTTP_400_BAD_REQUEST)
#
#         if booking_status != "Reserved":
#             return Response({"Reserv": "Вы не бронировали Номер"}, status=status.HTTP_400_BAD_REQUEST)
#
#         return self.create(request, *args, **kwargs)
#
#
# class BookingRestaurantView(generics.CreateAPIView):
#     serializer_class = BookingRestaurantSerializer
#
#     def post(self, request, *args, **kwargs):
#         booking_status = request.data['booking_status']
#         # print(booking_status)
#
#         bd = request.data['booking_date']
#         reserv_num = int(request.data['reserv_num'])
#         bd_t = request.data['booking_time']
#         if booking_status != "Reserved":
#             return Response({"Reserv": "Вы не бронировали Номер"}, status=status.HTTP_400_BAD_REQUEST)
#         return self.create(request, *args, **kwargs)
#
#
# class CancellationReserv(generics.RetrieveUpdateDestroyAPIView):
#     queryset = BookingHotel.objects.all()
#     serializer_class = BookingHotelSerializer
#     lookup_field = 'pk'
#
#     def delete(self, request, *args, **kwargs):
#         # reserv = self.request['booking_status']
#         query = self.queryset.filter(pk=self.kwargs['pk'])
#         query.delete()
#         return Response(
#             {"Delete": "Ваш бронь успешно отменен"},
#             status=status.HTTP_200_OK
#         )
#
#     def get_queryset(self):
#         return self.queryset.filter(pk=self.kwargs['pk'])
