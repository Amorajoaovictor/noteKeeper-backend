# Generated by Django 4.2 on 2023-04-04 20:34

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('polls', '0002_user0'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='User0',
            new_name='Userr0',
        ),
    ]
