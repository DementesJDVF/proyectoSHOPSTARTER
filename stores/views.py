from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.core.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404

from .forms import StoreForm
from .models import Store


@login_required
def create_store(request):
    if not request.user.is_seller():
        raise PermissionDenied

    # Evitar que cree más de un estante
    if hasattr(request.user, 'store'):
        return redirect('store_detail', pk=request.user.store.pk)

    if request.method == 'POST':
        form = StoreForm(request.POST)
        if form.is_valid():
            store = form.save(commit=False)
            store.owner = request.user
            store.save()
            return redirect('store_detail', pk=store.pk)
    else:
        form = StoreForm()

    return render(request, 'stores/create_store.html', {'form': form})

def store_detail(request, pk):
    store = get_object_or_404(Store, pk=pk, is_active=True)
    return render(request, 'stores/store_detail.html', {'store': store})

