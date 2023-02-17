from django import forms
from .models import Order
from phonenumber_field import formfields
from django.core.validators import EmailValidator


class OrderCreateForm(forms.ModelForm):

    class Meta:
        model = Order

        fields = ['first_name', 'last_name', 'email','country','city','delivery_method','method_of_payment', 'address','phone','comment','id_of_PVZ']
        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': 'Имя',
                                                 'class':'name'} ),
            'last_name': forms.TextInput(attrs={'placeholder': 'Фамилия',
                                                'class':'surname'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Email',
                                            'class':'email'}),
            'phone': forms.TextInput(attrs={'placeholder': 'Телефон',
                                            'class':'phone'},),
            'country':forms.TextInput(attrs={'placeholder': 'Страна(заполняется на русском языке)',
                                            'class':'country'},),

            'city': forms.TextInput(attrs={'placeholder': 'Город(заполняется на русском языке)',
                                           'class':'city'}),

            'address': forms.TextInput(attrs={'placeholder': 'Адрес(название улицы,номер дома, квартиры)',
                                              'class':'adress'}),

            'delivery_method':forms.RadioSelect(attrs={'placeholder': 'Метод доставки',
                                                         'class':'method_of_delivery'}),

            'method_of_payment':forms.RadioSelect(attrs={'placeholder': 'Метод оплаты',
                                                         'class':'method_of_payment'}),

            'comment':forms.Textarea(attrs={'placeholder': 'Комментарий',
                                              'class':'comment'}),
            'id_of_PVZ':forms.TextInput(attrs={'class':'id_of_PVZ'})
        }


