from django.contrib import admin
from .models import City, Hotels, Restaurants, Booking
admin.site.register(City)
admin.site.register(Hotels)
admin.site.register(Restaurants)
admin.site.register(Booking)