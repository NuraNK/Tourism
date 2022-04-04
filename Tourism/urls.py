from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path, include

urlpatterns_v1 = [
    path('user/', include('accounts.urls')),
    path('blog/', include('blog.urls')),
    path('tour_pack/', include('tour_pack.urls'))
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(urlpatterns_v1))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)