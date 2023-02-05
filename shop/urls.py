
from django.urls import path
from .views import *
urlpatterns = [
    path('',ListProducts.as_view()),
    path('about_us/',about_us,name='about_us'),
    path('search/', Search.as_view(),name='search'),
    path('products/<int:pk>',DetailProduct.as_view(),name='product_detail'),
]