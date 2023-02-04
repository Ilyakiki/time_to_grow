# Generated by Django 4.1.5 on 2023-01-30 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=200)),
                ('slug', models.SlugField(default='', max_length=200)),
                ('image', models.ImageField(blank=True, upload_to='products/')),
                ('description', models.TextField(blank=True)),
                ('structure', models.TextField(blank=True)),
                ('method_of_application', models.TextField(blank=True)),
                ('price', models.PositiveIntegerField(max_length=10)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ('name',),
                'index_together': {('id', 'slug')},
            },
        ),
    ]