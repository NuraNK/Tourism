from django.urls import path, include
from .views import RatingCreateView, RatingUpdateView, RatingListView, BlogListView, ReviewView, ReviewListView, BlogCreateView, BlogUpdateDestroyView,RatingDestroyView,ImageUploadView

urlpatterns = [
    path('rating-star/', RatingCreateView.as_view()),
    path('rating-star/update/<int:blog_id>/', RatingUpdateView.as_view()),
    path('rating-star/destroy/<int:blog_id>/', RatingDestroyView.as_view()),
    path('rating-star/<int:blog_id>/', RatingListView.as_view()),
    path('list/<int:blog_id>/', BlogListView.as_view()),
    path('create/', BlogCreateView.as_view()),
    path('image-create/', ImageUploadView.as_view()),
    path('update-destroy/<int:pk>/', BlogUpdateDestroyView.as_view()),
    path('review/', ReviewView.as_view()),
    path('review-list/<int:blog_id>/', ReviewListView.as_view()),

]