# Generated by Django 5.1.4 on 2025-01-29 14:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0003_dsa'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Customer',
        ),
        migrations.DeleteModel(
            name='DSA',
        ),
    ]
