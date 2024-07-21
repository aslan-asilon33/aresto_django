from django.shortcuts import render
# from . models import User

def hr_dashboard(request):
    return render(request, 'hr_dashboard/hr_dashboard.html')