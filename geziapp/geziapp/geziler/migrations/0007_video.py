# Generated by Django 4.1.3 on 2022-11-20 14:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('geziler', '0006_category_titleforhead_alter_category_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('url', models.CharField(max_length=200)),
                ('gezi', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='geziler.category')),
            ],
        ),
    ]
