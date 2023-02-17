from django.shortcuts import render
from .models import OrderItem
from .forms import OrderCreateForm
from cart.cart import Cart
import requests
import json

def Russia(form,cart):
    items = []
    if form.cleaned_data.get('method_of_payment') == '0':
        for item in cart:

            item_dict = {
                'name': item['product'].name,
                'ware_key': item['product'].id,
                "payment": {
                    "value": 0
                },
                "cost": item['product'].price,
                "weight": item['product'].weight,
                "amount": item['quantity']
            }
            items.append(item_dict)
    else:
        for item in cart:
            item_dict = {
                'name': item['product'].name,
                'ware_key': item['product'].id,
                "payment": {
                    "value": float(item['product'].price)
                },
                "cost": item['product'].price,
                "weight": item['product'].weight,
                "amount": item['quantity']
            }
            items.append(item_dict)
    first_name = form.cleaned_data.get('first_name')
    last_name = form.cleaned_data.get('last_name')
    phone = str(form.cleaned_data.get('phone'))
    if form.cleaned_data.get('delivery_method')=='0':
        id_of_pvz = form.cleaned_data.get('id_of_PVZ')
        data = {
            "type": 1,
            "tariff_code": 136,
            "shipment_point": 'SPB250',
            "delivery_point": id_of_pvz,
            "recipient": {
                "name": first_name + ' ' + last_name,
                "phones": [{
                    "number": phone
                }]
            },
            "packages": [{
                "number": 1,
                "weight": cart.get_total_weight(),
                "items": items,
                'length': 20,
                'width': 10,
                'height': 30
            }]
        }
    else:
        adress=form.cleaned_data.get('address')
        town=form.cleaned_data.get('town')
        data = {
            "type": 1,
            "tariff_code": 137,
            "shipment_point": 'SPB250',
            "to_location": {
                'city':town,
                'address':adress
            },
            "recipient": {
                "name": first_name + ' ' + last_name,
                "phones": [{
                    "number": phone
                }]
            },
            "packages": [{
                "number": 1,
                "weight": cart.get_total_weight(),
                "items": items,
                'length': 20,
                'width': 10,
                'height': 30
            }]
        }

    return data
def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()

            url_auth = 'https://api.edu.cdek.ru/v2/oauth/token?grant_type=client_credentials&client_id=EMscd6r9JnFiQ3bLoyjJY6eM78JrJceI&client_secret=PjLZkKBHEiLK3YsjtNrt3TGNG0ahs3kG'
            x = requests.post(url=url_auth)
            print(x.json())

            for item in cart:
                OrderItem.objects.create(order=order,
                                         product=item['product'],
                                         price=item['price'],
                                         quantity=item['quantity'])
            # очистка корзины


            if form.cleaned_data.get('country').capitalize in ['РОССИЯ','РФ','РОССИЙСКАЯ ФЕДЕРАЦИЯ']:
                data=Russia(form,cart)
            else:
                data=Russia(form,cart) #заменить на международные заказы

            data=json.dumps(data,ensure_ascii=False).encode('utf8')
            y=requests.post(url='https://api.edu.cdek.ru/v2/orders',data=data,headers={'Authorization':'Bearer'+' '+x.json()['access_token'],"Content-Type": "application/json"})
            print(data)
            print(y.json())
            cart.clear()

            return render(request, 'orders/order/created.html',
                          {'order': order})
    else:
        form = OrderCreateForm
    return render(request, 'orders/order/create.html',
                  {'cart': cart, 'form': form})