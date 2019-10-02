# Generated by Django 2.2.5 on 2019-10-01 08:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0015_remove_video_most_viewed'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='latest',
            field=models.BooleanField(default=False, verbose_name='Do you want this video to display in latest section?'),
        ),
    ]