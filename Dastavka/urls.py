
from django.contrib import admin
from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,

from asosiy.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('suvlar/', SuvlarAPI.as_view()),
    path('suvlar/<int:pk>/', SuvAPI.as_view()),
    path('mijozlar/<int:pk>/', MijozAPI.as_view()),
    path('mijozlar/', MijozlarAPI.as_view()),
    path('buyurtmalar/', BuyurtmalarAPI.as_view()),
    path('token_olish/', TokenObtainPairView.as_view()),
    path('token_yangilash/', TokenRefreshView.as_view()),

]
