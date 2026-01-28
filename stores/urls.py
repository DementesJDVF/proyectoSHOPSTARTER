from django.urls import path
from .views import create_store, store_detail

urlpatterns = [
    path('create/', create_store, name='store_create'),
    path('<int:pk>/', store_detail, name='store_detail'),
]
