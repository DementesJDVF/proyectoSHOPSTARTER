from django.urls import path
from .views import store_list, create_store, store_detail

urlpatterns = [
    path('', store_list, name='store_list'),
    path('create/', create_store, name='store_create'),
    path('<int:pk>/', store_detail, name='store_detail')
]
