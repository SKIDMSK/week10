# Generated by Django 5.0.8 on 2024-09-09 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='news_images', verbose_name='画像'),
        ),
    ]
