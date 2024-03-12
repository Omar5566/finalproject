from django.urls import path
from . import views

app_name = 'shop'
urlpatterns = [
    path('', views.home, name='home'),
    path('products/', views.product_list, name='product_list'),
    path('product-list/', views.product_list, name='product_list'),
]
