from django.shortcuts import render, redirect
from .forms import ClientRegisterForm, SellerRegisterForm
from django.contrib.auth import login
from django.contrib.auth.views import LoginView

class CustomLoginView(LoginView):
    template_name = 'users/login.html'

def register_client(request):
    if request.method == 'POST':
        form = ClientRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = ClientRegisterForm()

    return render(request, 'users/register_client.html', {'form': form})

def register_seller(request):
    if request.method == 'POST':
        form = SellerRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = SellerRegisterForm()

    return render(request, 'users/register_seller.html', {'form': form})

