# Generated by Django 3.2.8 on 2021-10-11 22:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shows', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='show',
            name='image',
        ),
    ]