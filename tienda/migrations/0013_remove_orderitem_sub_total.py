# Generated by Django 3.2.4 on 2021-07-06 01:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0012_auto_20210705_2047'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderitem',
            name='sub_total',
        ),
    ]