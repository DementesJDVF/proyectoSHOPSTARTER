from django.urls import path
from .views import create_store

urlpatterns = [
    path('create/', create_store, name='store_create'),
]
