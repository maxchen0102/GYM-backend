# Generated by Django 4.2.13 on 2024-06-07 11:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('personPage', '0004_alter_list_item_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='list',
            old_name='item_id',
            new_name='item',
        ),
    ]
