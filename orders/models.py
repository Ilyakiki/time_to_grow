from django.db import models
from shop.models import Product
from phonenumber_field.modelfields import PhoneNumberField

class Order(models.Model):

    first_name = models.CharField(max_length=50,blank=False)
    last_name = models.CharField(max_length=50,blank=False)
    email = models.EmailField(blank=False)
    phone=PhoneNumberField('RU',null=False,blank=False)
    country=models.CharField(max_length=100,default=None,blank=False)
    city = models.CharField(max_length=100,blank=False)
    address = models.CharField(max_length=250,blank=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    CHOISES_OF_METHOD_DELIVERY=(
        ('0','До пункта самовывоза СДЭК'),
    )
    delivery_method=models.CharField(blank=False,max_length=31,default=None,choices=CHOISES_OF_METHOD_DELIVERY)

    TYPE_SELECT = (
        ('0', 'Оплата Картой Онлайн'),
        ('1', 'Оплата при получении'),
    )

    method_of_payment=models.CharField(blank=False,max_length=31,default=None,choices=TYPE_SELECT)
    id_of_PVZ=models.CharField(blank=True,default=None,max_length=15,null=True)
    paid = models.BooleanField(default=False)
    comment=models.TextField(default=None,blank=True)


    class Meta:
        ordering = ('-created',)
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return 'Order {}'.format(self.id)

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items',on_delete = models.CASCADE)
    product = models.ForeignKey(Product, related_name='order_items',on_delete = models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return '{}'.format(self.id)

    def get_cost(self):
        return self.price * self.quantity