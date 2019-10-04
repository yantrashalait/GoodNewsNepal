from django.contrib import admin
from .models import Video, BigBanner, SmallBanner, Category, AboutUs

# Register your models here.
admin.site.register(Video)
admin.site.register(BigBanner)
admin.site.register(SmallBanner)
admin.site.register(Category)
admin.site.register(AboutUs)