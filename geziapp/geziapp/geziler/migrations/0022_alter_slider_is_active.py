# Generated by Django 4.1.3 on 2022-12-08 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('geziler', '0021_slider_is_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slider',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
    ]
