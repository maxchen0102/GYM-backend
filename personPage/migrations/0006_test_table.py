# Generated by Django 4.2.13 on 2024-06-26 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personPage', '0005_rename_item_id_list_item'),
    ]

    operations = [
        migrations.CreateModel(
            name='test_table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('age', models.IntegerField(null=True)),
            ],
        ),
    ]