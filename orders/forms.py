from django import forms
from .models import Order
from phonenumber_field import formfields
from django.core.validators import EmailValidator


class OrderCreateForm(forms.ModelForm):

    class Meta:
        model = Order

        fields = ['first_name', 'last_name', 'email', 'address','phone','city']
        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': 'Имя',
                                                 'class':'name'} ),
            'last_name': forms.TextInput(attrs={'placeholder': 'Фамилия',
                                                'class':'surname'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Email',
                                            'class':'email'}),
            'phone': forms.TextInput(attrs={'placeholder': 'Телефон',
                                            'class':'phone'},),
            'address': forms.TextInput(attrs={'placeholder': 'Адрес'}),
            'city': forms.TextInput(attrs={'placeholder': 'Город'}),
        }
