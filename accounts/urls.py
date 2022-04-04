from django.urls import path, include
from .views import UserRegisterView,LoginView

urlpatterns = [
    path('register/', UserRegisterView.as_view()),
    path('login/', LoginView.as_view()),
]