# Generated by Django 2.2.5 on 2019-11-03 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0023_aboutus_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='aboutus',
            name='title',
            field=models.CharField(blank=True, max_length=400, null=True),
        ),
    ]
