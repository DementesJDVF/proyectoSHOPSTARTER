from django.urls import path
from .views import (
    cart_add,
    cart_detail,
    cart_update,
    cart_remove
)

urlpatterns = [
    path('add/<int:product_id>/', cart_add, name='cart_add'),
    path('', cart_detail, name='cart_detail'),
    path('update/<int:product_id>/', cart_update, name='cart_update'),
    path('remove/<int:product_id>/', cart_remove, name='cart_remove'),
]
