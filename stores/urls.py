from django.urls import path
from .views import create_store, store_detail, store_list, seller_dashboard

urlpatterns = [
    path('', store_list, name='store_list'),
    path('dashboard/', seller_dashboard, name='seller_dashboard'),
    path('create/', create_store, name='store_create'),
    path('<int:pk>/', store_detail, name='store_detail'),
]
