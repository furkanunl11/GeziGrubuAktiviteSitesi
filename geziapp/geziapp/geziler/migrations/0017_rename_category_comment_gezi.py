# Generated by Django 4.1.3 on 2022-11-21 11:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('geziler', '0016_alter_comment_category'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='category',
            new_name='gezi',
        ),
    ]
