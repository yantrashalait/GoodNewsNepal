from django.db import models
from django.utils import timezone

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=300)

    def __str__(self):
        return self.name

class Video(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='video')
    video_url = models.URLField(help_text="Please enter the url of the video from youtube or other sources")
    thumbnail_image = models.ImageField(upload_to='thumbnail/')
    video_caption = models.TextField()
    video_description = models.TextField()
    date = models.DateField()
    recommend = models.BooleanField(default=False, verbose_name='Do you want this video to display in recommend section?')
    latest = models.BooleanField(default=False, verbose_name='Do you want this video to display in latest section?')
    featured = models.BooleanField(default=False, verbose_name='Do you want this video to display in featured section?')

    def __str__(self):
        return self.video_caption
    

class BigBanner(models.Model):
    main_image = models.ImageField(upload_to='banner/', null=True, blank=True)
    company_name = models.CharField(max_length=200, null=True, blank=True)
    added_date = models.DateField(default=timezone.now)
    valid_date = models.DateField()
    show = models.BooleanField(default=True)

class SmallBanner(models.Model):
    image = models.ImageField(upload_to='banner/', null=True, blank=True)
    company_name = models.CharField(max_length=200, null=True, blank=True)
    added_date = models.DateField(default=timezone.now)
    valid_date = models.DateField()
    show = models.BooleanField(default=True)

