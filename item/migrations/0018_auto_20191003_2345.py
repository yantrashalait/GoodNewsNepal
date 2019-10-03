# Generated by Django 2.2.5 on 2019-10-03 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0017_video_featured'),
    ]

    operations = [
        migrations.AddField(
            model_name='bigbanner',
            name='company_link',
            field=models.URLField(blank=True, help_text='Please enter the url of company', null=True),
        ),
        migrations.AlterField(
            model_name='bigbanner',
            name='main_image',
            field=models.ImageField(blank=True, help_text='Image size: width=1024px height=77px', null=True, upload_to='banner/'),
        ),
        migrations.AlterField(
            model_name='smallbanner',
            name='image',
            field=models.ImageField(blank=True, help_text='Image size: width=1024px height=500px', null=True, upload_to='banner/'),
        ),
        migrations.AlterField(
            model_name='video',
            name='thumbnail_image',
            field=models.ImageField(blank=True, help_text='Image size: width=1199px height=800px', null=True, upload_to='thumbnail/'),
        ),
        migrations.AlterField(
            model_name='video',
            name='video_description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
