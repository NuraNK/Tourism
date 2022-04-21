from django.urls import path

from tour_pack.views import ListTourView, ListCityView, RetrieveListTourView, CheckPlaceView, TourOrderList

urlpatterns = [
    path('list/<int:pk>/', RetrieveListTourView.as_view()),
    # path('create/comment/<int:blog_id>/', CreateCommentView.as_view()),
    path('list/', ListTourView.as_view()),
    path('city/', ListCityView.as_view()),
    path('order/', TourOrderList.as_view()),
    path('check-place/<int:pk>/', CheckPlaceView.as_view()),
]
