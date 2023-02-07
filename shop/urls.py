
from django.urls import path
from .views import *
urlpatterns = [
    path('',homepage,name='homepage'),
    path('products/',ListProducts.as_view(),name='list_products'),
    path('about_us/',about_us,name='about_us'),
    path('contacts/',contacts,name='contacts'),
    path('where_you_can_buy',where_buy,name='where_you_can_buy'),
    path('search/', Search.as_view(),name='search'),
    path('products/<int:pk>',DetailProduct.as_view(),name='product_detail'),
]