# Generated by Django 2.2.5 on 2019-10-04 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0020_auto_20191003_2355'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutUs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=200)),
                ('contact_number', models.CharField(max_length=20)),
                ('youtube_link', models.URLField(help_text='Enter youtube url')),
                ('facebook_link', models.URLField(help_text='Enter facebook url')),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='banner/')),
            ],
        ),
    ]