from django.urls import path, include
from .views import UserRegisterView, LoginView, ProfileInfoVIew

urlpatterns = [
    path('register/', UserRegisterView.as_view()),
    path('login/', LoginView.as_view()),
    path('me/', ProfileInfoVIew.as_view(), name='auth_me'),  # Профиль
]