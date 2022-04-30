from django.urls import path
from .views import ListHotelView, CreateHotelView, CreateRateView, \
    CreateRoomView, ListRoomHotelView, \
    CreateRateRoomView, DetailHotelView, OurRoomsView, BookingView, \
    RoomUpdateDestroyView, UpdateDestroyHotelView, DeleteBookingView, \
    IndexHotelView, IndexRoomView

urlpatterns = [
    path('list/', ListHotelView.as_view()),
    path('list/<int:pk>/', DetailHotelView.as_view()),

    path('list/<int:hotel_id>/<int:pk>/', ListRoomHotelView.as_view()),
    path('list/<int:hotel_id>/room/', OurRoomsView.as_view()),

    path('create/', CreateHotelView.as_view()),
    path('detail/<int:pk>/', UpdateDestroyHotelView.as_view()),

    path('create/room/', CreateRoomView.as_view()),
    path('detail/<int:hotel_id>/room/<int:pk>/',
         RoomUpdateDestroyView.as_view()),

    path('create/rate/<int:hotel_id>/', CreateRateView.as_view()),
    path('create/rate/<int:hotel_id>/<int:room_id>/',
         CreateRateRoomView.as_view()),

    path('<int:hotel_id>/<int:room_id>/booking/', BookingView.as_view()),
    path('<int:hotel_id>/<int:room_id>/<int:order_num>/destroy/',
         DeleteBookingView.as_view()),

    path('list_index/', IndexHotelView.as_view()),
    path('list_index_room/', IndexRoomView.as_view()),

]
# from to price
