from django.db import models
from django.template.defaultfilters import slugify  # new
from django.urls import reverse


# Create your models here.
class VideoModel(models.Model):
    name = models.CharField(max_length=255)
    video = models.FileField(upload_to='videos/')
    slug = models.SlugField(null=False, unique=True)
    joined_date = models.DateTimeField(auto_now=True)

    
    def get_absolute_url(self):
        return reverse("article_detail", kwargs={"slug": self.slug})

    def save(self, *args, **kwargs):  # new
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)
    
    def __str__(self) -> str:
        return self.name