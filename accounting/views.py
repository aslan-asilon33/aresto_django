from django.shortcuts import render
# from .models import User

def dashboard_accounting(request):
    # users = User.objects.all()
    # return render(request, 'users/user_list.html', {'users': users})
    return render(request, 'dashboard_accounting/dashboard_accounting.html')