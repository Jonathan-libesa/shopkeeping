from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='homepage'),
    path('products/add/', views.product_create, name='product_create'),
]