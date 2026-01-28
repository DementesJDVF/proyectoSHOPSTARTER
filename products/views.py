from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.shortcuts import render, redirect, get_object_or_404

from .models import Product
from .forms import ProductForm


@login_required
def product_list(request):
    if not request.user.is_seller():
        raise PermissionDenied

    store = getattr(request.user, 'store', None)
    products = Product.objects.filter(store=store)

    return render(
        request,
        'products/product_list.html',
        {'products': products}
    )


@login_required
def product_create(request):
    if not request.user.is_seller():
        raise PermissionDenied

    store = getattr(request.user, 'store', None)

    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            product = form.save(commit=False)
            product.store = store
            product.save()
            return redirect('product_list')
    else:
        form = ProductForm()

    return render(
        request,
        'products/product_form.html',
        {'form': form}
    )
