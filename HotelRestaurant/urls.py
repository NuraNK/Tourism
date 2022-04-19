from django.urls import path
from .views import ListHotelView,CreateHotelView, CreateRateView, CreateRoomView, ListRoomHotelView, CreateRateRoomView

urlpatterns = [
    path('list/', ListHotelView.as_view()),
    path('create/', CreateHotelView.as_view()),
    path('create/room/', CreateRoomView.as_view()),
    path('create/rate/<int:hotel_id>/', CreateRateView.as_view()),
    path('create/rate/<int:hotel_id>/<int:room_id>/', CreateRateRoomView.as_view()),
]