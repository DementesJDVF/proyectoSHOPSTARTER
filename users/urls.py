from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/client/', views.register_client, name='register_client'),
    path('register/seller/', views.register_seller, name='register_seller'),
]
