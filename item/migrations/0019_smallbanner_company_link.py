# Generated by Django 2.2.5 on 2019-10-03 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0018_auto_20191003_2345'),
    ]

    operations = [
        migrations.AddField(
            model_name='smallbanner',
            name='company_link',
            field=models.URLField(blank=True, help_text='Please enter the url of company', null=True),
        ),
    ]