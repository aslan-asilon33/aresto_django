from django.shortcuts import render

def product_dashboard(request):
    return render(request, 'product_dashboard/product_dashboard.html')