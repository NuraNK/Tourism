from django.contrib import admin
from .models import Rating, RatingStar, Reviews, Blog
# Register your models here.
admin.site.register(Rating)
admin.site.register(RatingStar)
admin.site.register(Reviews)
admin.site.register(Blog)
