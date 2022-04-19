from django.contrib import admin

# Register your models here.
from .models import City, Hotels, RoomsHotel,RateHotels, ReviewTotal, RateRoom
admin.site.register(City)
admin.site.register(Hotels)
admin.site.register(RoomsHotel)
admin.site.register(RateHotels)
admin.site.register(ReviewTotal)
admin.site.register(RateRoom)