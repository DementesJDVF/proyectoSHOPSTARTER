from django.shortcuts import get_object_or_404, redirect, render
from products.models import Product
from django.contrib import messages
from .cart import Cart

def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.add(product=product)
    return redirect('cart_detail')

def cart_detail(request):
    cart = request.session.get('cart', {})
    cart_items = []

    for product_id, item in cart.items():
        product = Product.objects.get(id=product_id)
        cart_items.append({
            'product': product,
            'quantity': item['quantity'],
            'subtotal': product.price * item['quantity']
        })

    return render(
        request,
        'cart/cart_detail.html',
        {'cart_items': cart_items}
    )


def cart_update(request, product_id):
    cart = request.session.get('cart', {})
    product = get_object_or_404(Product, id=product_id)

    action = request.POST.get('action')

    if str(product_id) in cart:
        if action == 'increase':
            if cart[str(product_id)]['quantity'] < product.stock:
                cart[str(product_id)]['quantity'] += 1
            else:
                messages.warning(
                    request,
                    'No hay más stock disponible.'
                )

        elif action == 'decrease':
            cart[str(product_id)]['quantity'] -= 1
            if cart[str(product_id)]['quantity'] <= 0:
                del cart[str(product_id)]

    request.session['cart'] = cart
    return redirect('cart_detail')

def cart_remove(request, product_id):
    cart = request.session.get('cart', {})

    if str(product_id) in cart:
        del cart[str(product_id)]
        request.session['cart'] = cart

    return redirect('cart_detail')

