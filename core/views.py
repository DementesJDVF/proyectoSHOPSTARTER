from django.shortcuts import render

def home(request):
    return render(request, 'core/home.html')

def seller_dashboard(request):
    return render(request, 'core/seller_dashboard.html')

def client_dashboard(request):
    return render(request, 'core/client_dashboard.html')
