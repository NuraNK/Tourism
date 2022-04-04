from django.urls import path
from .views import CityView, HotelsCreateView, RestaurantsCreateView, BookingCreateView, CancellationReserv
urlpatterns = [
    path('city/', CityView.as_view()),
    path('hotel/', HotelsCreateView.as_view()),
    path('resaurant/', RestaurantsCreateView.as_view()),
    path('booking/', BookingCreateView.as_view()),
    path('booking/update-destroy/<int:pk>/', CancellationReserv.as_view()),
]