from django.urls import path

from . import views

urlpatterns = [
    path("", views.hr_dashboard, name="hr_dashboard"),
]