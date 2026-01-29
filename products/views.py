from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages

from .models import Product
from .forms import ProductForm
from stores.models import Store
from .forms import ProductImageForm

@login_required
def product_create(request):
    if not request.user.is_seller():
        raise PermissionDenied

    store = Store.objects.filter(owner=request.user).first()

    if not store:
        messages.warning(
            request,
            "Debes crear tu estante antes de añadir productos."
        )
        return redirect('store_create')

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

    
@login_required
def product_update(request, pk):
    if not request.user.is_seller():
        raise PermissionDenied

    product = get_object_or_404(Product, pk=pk)

    if product.store != request.user.store:
        raise PermissionDenied

    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm(instance=product)

    return render(
        request,
        'products/product_form.html',
        {'form': form, 'product': product}
    )


@login_required
def product_delete(request, pk):
    if not request.user.is_seller():
        raise PermissionDenied

    product = get_object_or_404(Product, pk=pk)

    if product.store != request.user.store:
        raise PermissionDenied

    if request.method == 'POST':
        product.delete()
        return redirect('product_list')

    return render(
        request,
        'products/product_confirm_delete.html',
        {'product': product}
    )

@login_required
def product_list(request):
    if not request.user.is_seller():
        raise PermissionDenied

    products = Product.objects.filter(store__owner=request.user)

    return render(
        request,
        'products/product_list.html',
        {'products': products}
    )
    
@login_required
def product_add_image(request, pk):
    product = get_object_or_404(
        Product,
        pk=pk,
        store__owner=request.user
    )

    if request.method == 'POST':
        form = ProductImageForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.product = product
            image.save()
            return redirect('product_list')
    else:
        form = ProductImageForm()

    return render(
        request,
        'products/product_image_form.html',
        {
            'form': form,
            'product': product
        }
    )
