from django.shortcuts import get_object_or_404, redirect, render
from products.models import Product
from .cart import Cart

def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.add(product=product)
    return redirect('cart_detail')

def cart_detail(request):
    cart = Cart(request)
    return render(
        request,
        'cart/cart_detail.html',
        {'cart': cart}
    )