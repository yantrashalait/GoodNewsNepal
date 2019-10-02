from django.contrib import admin
from .models import Video, BigBanner, SmallBanner, Category

# Register your models here.
admin.site.register(Video)
admin.site.register(BigBanner)
admin.site.register(SmallBanner)
admin.site.register(Category)