from django.contrib import admin

from .models import Product,MainIngridient,DescriptionPoint
# Register your models here.
class DescriptionPointAdmin(admin.ModelAdmin):
    list_display = ['name']
    list_filter = ['name']

class MainIngridientAdmin(admin.ModelAdmin):
    list_display = ['name']
    list_filter = ['name']

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'created', 'updated','available','slug']
    list_filter = ['created', 'updated','available']
    list_editable = ['price','available']
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Product, ProductAdmin)
admin.site.register(MainIngridient, MainIngridientAdmin)
admin.site.register(DescriptionPoint, DescriptionPointAdmin)