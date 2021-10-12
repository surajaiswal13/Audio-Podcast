# Generated by Django 3.2.8 on 2021-10-12 14:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('shows', '0003_show_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Episode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256, unique=True)),
                ('episode_slug', models.SlugField(allow_unicode=True, unique=True)),
                ('description', models.TextField(blank=True, default='')),
                ('image', models.ImageField(blank=True, upload_to='episode_images')),
                ('audio', models.FileField(blank=True, upload_to='episode_audios')),
                ('show', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='shows', to='shows.show')),
            ],
        ),
    ]
