# Generated by Django 2.2.5 on 2019-09-29 09:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0010_video_recent'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='video',
            name='recent',
        ),
    ]