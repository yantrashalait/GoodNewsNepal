# Generated by Django 2.2.5 on 2019-09-19 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0002_banner'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='banner',
            name='image',
        ),
        migrations.AddField(
            model_name='banner',
            name='main_image',
            field=models.ImageField(blank=True, null=True, upload_to='banner/'),
        ),
        migrations.AddField(
            model_name='banner',
            name='small_image',
            field=models.ImageField(blank=True, null=True, upload_to='banner/small/'),
        ),
    ]
