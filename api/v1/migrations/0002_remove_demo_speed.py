# Generated by Django 4.2.1 on 2023-06-03 07:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('v1', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='demo',
            name='speed',
        ),
    ]
