from django.urls import path

from . import views

urlpatterns = [
    path("", views.marketing_dashboard, name="marketing_dashboard"),
]