from django.urls import path
from . import views

urlpatterns = [
    path('register/client/', views.register_client, name='register_client'),
    path('register/seller/', views.register_seller, name='register_seller'),
]
