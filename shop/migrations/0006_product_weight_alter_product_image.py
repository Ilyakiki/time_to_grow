# Generated by Django 4.1.5 on 2023-02-16 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_product_short_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='weight',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(upload_to='products/'),
        ),
    ]
