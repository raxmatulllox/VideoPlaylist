from django.contrib import admin
from .models import VideoModel


# Register your models here.
class VideoModelAdmin(admin.ModelAdmin):
  list_display = ('name', 'joined_date', 'video')
  prepopulated_fields = {"slug": ("name",)}
  
admin.site.register(VideoModel, VideoModelAdmin)