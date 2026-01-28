from django.urls import path
from .views import home, seller_dashboard, client_dashboard

urlpatterns = [
    path('', home, name='home'),
    path('seller/', seller_dashboard, name='seller_dashboard'),
    path('client/', client_dashboard, name='client_dashboard'),
]
