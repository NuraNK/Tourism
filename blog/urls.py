from django.urls import path, include
from .views import CreateBlogView, RetrieveListBlogView, CreateCommentView, \
    CreateRateView, UpdateBlogView, ListCommentView, ListBlogView, \
    ListCategoryView, DeleteCommentView,RecentBLogView

urlpatterns = [
    path('create/', CreateBlogView.as_view()),
    path('list/<int:pk>/', RetrieveListBlogView.as_view()),
    path('detail/<int:pk>/', UpdateBlogView.as_view()),
    path('create/comment/<int:blog_id>/', CreateCommentView.as_view()),
    path('delete/comment/<int:blog_id>/<int:pk>/',
         DeleteCommentView.as_view()),
    path('create/rate/<int:blog_id>/', CreateRateView.as_view()),
    path('list/', ListBlogView.as_view()),                         #------------------GET BLOG LIST BY CATEGORY_ID
    path('list_recent/<int:blog_id>/', RecentBLogView.as_view()),  #-----------------------RECEN BLOG 10 ШТУК
    path('list-category/', ListCategoryView.as_view()),
    path('list-comment/<int:blog_id>/', ListCommentView.as_view()),
]


