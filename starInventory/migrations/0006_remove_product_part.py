# Generated by Django 4.0.3 on 2022-04-05 23:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('starInventory', '0005_auto_20220406_1136'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='part',
        ),
    ]
