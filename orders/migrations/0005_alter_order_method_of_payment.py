# Generated by Django 4.1.5 on 2023-02-11 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0004_order_comment_order_country_order_method_of_payment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='method_of_payment',
            field=models.CharField(choices=[('0', 'Оплата Картой Онлайн'), ('1', 'Оплата при получении')], default=None, max_length=31),
        ),
    ]
