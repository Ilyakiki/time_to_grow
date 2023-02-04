
from django.urls import path
from .views import *
urlpatterns = [
    path('',ListProducts.as_view()),
    path('search/', Search.as_view(),name='search'),
    path('products/<int:pk>',DetailProduct.as_view(),name='product_detail'),
]