from django.shortcuts import render, redirect
from .forms import ClientRegisterForm, SellerRegisterForm

def register_client(request):
    if request.method == 'POST':
        form = ClientRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = ClientRegisterForm()

    return render(request, 'users/register_client.html', {'form': form})
def register_seller(request):
    if request.method == 'POST':
        form = SellerRegisterForm(request.POST)
        if form.is_valid(): 
            form.save()
            return redirect('login')
    else:
        form = SellerRegisterForm()

    return render(request, 'users/register_seller.html', {'form': form})
