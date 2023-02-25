from django.shortcuts import render,redirect
from .models import OrderItem,Order
from .forms import OrderCreateForm
from cart.cart import Cart
import requests
import json
import uuid
from yookassa import Configuration, Payment
def Russia(form,cart,order):


    first_name = form.cleaned_data.get('first_name')
    last_name = form.cleaned_data.get('last_name')
    third_name=form.cleaned_data.get('third_name')
    phone = str(form.cleaned_data.get('phone'))
    if form.cleaned_data.get('delivery_method')=='0':
        id_of_pvz = form.cleaned_data.get('id_of_PVZ')
        data = {
            "type": 1,
            "tariff_code": 136,
            "number":str(order.id),
            "shipment_point": 'SPB284',
            "delivery_point": id_of_pvz,
            "recipient": {
                "name": last_name + ' ' + first_name + ' ' + third_name,
                "phones": [{
                    "number": phone
                }]
            },
            "packages": [{
                "number": 1,
                "weight": cart.get_total_weight(),
                "items": [],
                'length': 20,
                'width': 10,
                'height': 30
            }]
        }
    else:
        adress=form.cleaned_data.get('address')
        city=form.cleaned_data.get('city')
        data = {
            "type": 1,
            "tariff_code": 137,
            "shipment_point": 'SPB284',
            "number": str(order.id),
            "to_location": {
                'city':city,
                'address':adress
            },
            "recipient": {
                "name": last_name + ' ' + first_name + ' ' + third_name,
                "phones": [{
                    "number": phone
                }]
            },
            "packages": [{
                "number": 1,
                "weight": cart.get_total_weight(),
                "items": [],
                'length': 20,
                'width': 10,
                'height': 30
            }]
        }

    return data


def payment():
    pass
def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()



            if form.cleaned_data.get('method_of_payment')=='0':
                Configuration.account_id = '986433'
                Configuration.secret_key = 'test_5gO17B6ioJpDb-LF6-lD5SgbKj7YwC7JmbiKmTN9Efs'

                first_name = form.cleaned_data.get('first_name')
                last_name = form.cleaned_data.get('last_name')
                third_name = form.cleaned_data.get('third_name')
                phone = str(form.cleaned_data.get('phone'))
                email=str(form.cleaned_data.get('email'))
                goods=[]

                for item in cart:
                    good_dict={
                        "description":item['product'].name,
                        "quantity": item['quantity'],
                        "amount":{
                            "value": f"{item['product'].price}",
                            "currency": "RUB"
                        },
                        "vat_code": "1"
                    }
                    goods.append(good_dict)

                payment = Payment.create({
                    "amount": {
                        "value": f"{cart.get_total_price()}.00",
                        "currency": "RUB"
                    },
                    "confirmation": {
                        "type": "redirect",
                        "return_url": f"http://127.0.0.1:8000/orders/created/{order.id}"
                    },
                    "capture": True,
                    "description": f"Заказ №{order.id}",
                    "metadata": {'order_id':order.id},
                    "receipt":{
                        "customer":{
                            "full_name":last_name + ' ' + first_name + ' ' + third_name,
                            "phone":phone,
                            "email":email
                        },
                        "items":goods
                    },
                    "test": True,
                }, uuid.uuid4())
                order.payment_id=payment.id
                order.save()
                return redirect(payment.confirmation.confirmation_url,form=form)

            url_auth = 'https://api.edu.cdek.ru/v2/oauth/token?grant_type=client_credentials&client_id=EMscd6r9JnFiQ3bLoyjJY6eM78JrJceI&client_secret=PjLZkKBHEiLK3YsjtNrt3TGNG0ahs3kG'
            x = requests.post(url=url_auth)
            print(x.json())

            items = []
            for item in cart:
                OrderItem.objects.create(order=order,
                                         product=item['product'],
                                         price=item['price'],
                                         quantity=item['quantity'])
                if form.cleaned_data.get('method_of_payment')=='1':
                    item_dict = {
                        'name': item['product'].name,
                        'ware_key': item['product'].id,
                        "payment": {
                            "value": float(item['product'].price)
                        },
                        "cost": float(item['product'].price),
                        "weight": item['product'].weight,
                        "amount": item['quantity']
                    }
                    items.append(item_dict)

            data = Russia(form, cart,order)
            data['packages'][0]['items'] = items
            print(data)
            data = json.dumps(data, ensure_ascii=False).encode('utf8')
            y=requests.post(url='https://api.edu.cdek.ru/v2/orders',data=data,headers={'Authorization':'Bearer'+' '+x.json()['access_token'],"Content-Type": "application/json"})
            order.sended_to_sdek=True
            order.save()
            print(y.json())

            # очистка корзины
            cart.clear()

            return render(request, 'orders/order/created.html',
                          {'order': order})
    else:
        form = OrderCreateForm
    return render(request, 'orders/order/create.html',
                  {'cart': cart, 'form': form})


def order_created(request,id_order):
    cart = Cart(request)
    order=Order.objects.get(id=id_order)
    url_auth = 'https://api.edu.cdek.ru/v2/oauth/token?grant_type=client_credentials&client_id=EMscd6r9JnFiQ3bLoyjJY6eM78JrJceI&client_secret=PjLZkKBHEiLK3YsjtNrt3TGNG0ahs3kG'
    x = requests.post(url=url_auth)
    payment_id=order.payment_id
    one_payment = Payment.find_one(payment_id)
    if order.sended_to_sdek==True or one_payment.status!='succeeded':
        return redirect('shop:homepage')
    else:



        print(x.json())

        items = []
        for item in cart:
            OrderItem.objects.create(order=order,
                                     product=item['product'],
                                     price=item['price'],
                                     quantity=item['quantity'])

            item_dict = {
                'name': item['product'].name,
                'ware_key': item['product'].id,
                "payment": {
                    "value": 0.00
                },
                "cost": float(item['product'].price),
                "weight": item['product'].weight,
                "amount": item['quantity']
            }
            items.append(item_dict)


        first_name = order.first_name
        last_name = order.last_name
        third_name = order.third_name
        phone = str(order.phone)

        print(phone)

        if order.delivery_method == '0':
            id_of_pvz = order.id_of_PVZ
            data = {
                "type": 1,
                "tariff_code": 136,
                "number": str(order.id),
                "shipment_point": 'SPB284',
                "delivery_point": id_of_pvz,
                "recipient": {
                    "name": last_name + ' ' + first_name + ' ' + third_name,
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
            adress = order.address
            city = order.city
            data = {
                "type": 1,
                "tariff_code": 137,
                "number": str(order.id),
                "shipment_point": 'SPB284',
                "to_location": {
                    'city': city,
                    'address': adress
                },
                "recipient": {
                    "name": last_name + ' ' + first_name + ' ' + third_name,
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
        print(data)
        data = json.dumps(data, ensure_ascii=False).encode('utf8')
        y = requests.post(url='https://api.edu.cdek.ru/v2/orders', data=data,
                          headers={'Authorization': 'Bearer' + ' ' + x.json()['access_token'],
                                   "Content-Type": "application/json"})
        print(y.json())
        order.sended_to_sdek = True
        order.save()
        cart.clear()

    return render(request,'orders/order/created.html',{'order':order})