# Generated by Django 4.0.5 on 2022-06-21 18:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0016_auto_20210705_2228'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='cliente',
        ),
        migrations.RemoveField(
            model_name='orderitem',
            name='items',
        ),
        migrations.RemoveField(
            model_name='orderitem',
            name='order',
        ),
        migrations.DeleteModel(
            name='datosEnvio',
        ),
        migrations.DeleteModel(
            name='Order',
        ),
        migrations.DeleteModel(
            name='OrderItem',
        ),
    ]
