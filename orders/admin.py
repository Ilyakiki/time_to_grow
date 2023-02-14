from django.contrib import admin
from .models import Order, OrderItem


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['product']


class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'email','country','city',
                    'address','method_of_payment',  'paid',
                    'created', 'updated']
    list_filter = ['paid', 'created', 'updated','method_of_payment']
    inlines = [OrderItemInline]

admin.site.register(Order, OrderAdmin)