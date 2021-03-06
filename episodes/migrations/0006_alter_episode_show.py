# Generated by Django 3.2.8 on 2021-10-12 21:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shows', '0004_auto_20211012_2253'),
        ('episodes', '0005_alter_episode_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='episode',
            name='show',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='episodes', to='shows.show'),
        ),
    ]
