from django.db import models
from django.utils import timezone

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=300)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

class Video(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='video', null=True, blank=True)
    video_url = models.URLField(help_text="Please enter the url of the video from youtube or other sources")
    thumbnail_image = models.ImageField(upload_to='thumbnail/', help_text="Image size: width=1199px height=800px", null=True, blank=True)
    video_caption = models.TextField(null=True, blank=True)
    video_description = models.TextField(null=True, blank=True)
    date = models.DateField()
    recommend = models.BooleanField(default=False, verbose_name='Do you want this video to display in recommend section?')
    latest = models.BooleanField(default=False, verbose_name='Do you want this video to display in latest section?')
    featured = models.BooleanField(default=False, verbose_name='Do you want this video to display in featured section?')

    def __str__(self):
        return self.video_caption
    

class BigBanner(models.Model):
    main_image = models.ImageField(upload_to='banner/', help_text="Image size: width=1024px height=77px")
    company_name = models.CharField(max_length=200)
    company_link = models.URLField(help_text="Please enter the url of company")
    added_date = models.DateField(default=timezone.now)
    valid_date = models.DateField()
    show = models.BooleanField(default=True)

    def __str__(self):
        return self.company_name

class SmallBanner(models.Model):
    image = models.ImageField(upload_to='banner/', help_text="Image size: width=1024px height=500px")
    company_name = models.CharField(max_length=200)
    company_link = models.URLField(help_text="Please enter the url of company")
    added_date = models.DateField(default=timezone.now)
    valid_date = models.DateField()
    show = models.BooleanField(default=True)

    def __str__(self):
        return self.company_name

class AboutUs(models.Model):
    company_name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    email = models.EmailField(null=True, blank=True)
    contact_number = models.CharField(max_length=20)
    youtube_link = models.URLField(help_text="Enter youtube url")
    facebook_link = models.URLField(help_text="Enter facebook url")
    title = models.CharField(max_length=400, null=True, blank=True)
    description = models.TextField()
    image = models.ImageField(upload_to='banner/')

    def __str__(self):
        return self.company_name

