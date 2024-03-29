# Generated by Django 2.2.5 on 2019-09-19 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0004_auto_20190919_1510'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bigbanner',
            old_name='valied_date',
            new_name='valid_date',
        ),
        migrations.RenameField(
            model_name='smallbanner',
            old_name='valied_date',
            new_name='valid_date',
        ),
        migrations.AddField(
            model_name='bigbanner',
            name='company_name',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='bigbanner',
            name='show',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='smallbanner',
            name='show',
            field=models.BooleanField(default=True),
        ),
    ]
