# Generated by Django 4.2 on 2023-04-04 22:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0004_remove_user_password'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='note',
            name='test',
        ),
    ]
