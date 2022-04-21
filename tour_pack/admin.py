from django.contrib import admin

from tour_pack.models import Place, Gallery, Tour, TourOrder, UserTour

admin.site.register(Place)
admin.site.register(Gallery)
admin.site.register(Tour)
admin.site.register(UserTour)


@admin.register(TourOrder)
class UserTourTourAdmin(admin.ModelAdmin):
    list_display = ('user', 'count', 'name', 'phone', 'tour', 'created', 'confirm')
    search_fields = ["name", "phone"]
    list_filter = ['tour', 'confirm']