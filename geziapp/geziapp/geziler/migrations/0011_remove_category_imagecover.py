# Generated by Django 4.1.3 on 2022-11-21 07:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('geziler', '0010_category_imagecover_alter_category_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='imagecover',
        ),
    ]