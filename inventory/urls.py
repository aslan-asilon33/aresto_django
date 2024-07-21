from django.urls import path

from . import views

urlpatterns = [
    path("", views.product_dashboard, name="product_dashboard"),
]