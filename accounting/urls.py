from django.urls import path

from . import views

urlpatterns = [
    path("", views.dashboard_accounting, name="dashboard_accounting"),
]