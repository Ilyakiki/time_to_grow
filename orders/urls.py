from django.urls import path
from . import views


urlpatterns = [
    path('create/', views.order_create, name='order_create'),
    path('created/<int:id_order>', views.order_created, name='order_created'),
]
app_name='orders'