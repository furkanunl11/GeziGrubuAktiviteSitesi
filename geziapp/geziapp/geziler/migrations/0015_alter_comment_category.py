# Generated by Django 4.1.3 on 2022-11-21 11:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('geziler', '0014_comment_date_added_alter_comment_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='geziler.category'),
        ),
    ]
