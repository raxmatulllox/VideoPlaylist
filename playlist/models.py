from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse


# Create your models here.
class VideoModel(models.Model):
    name = models.CharField(max_length=255, unique=True)
    video = models.FileField(upload_to='videos/')
    slug = models.SlugField(null=False, unique=True)
    joined_date = models.DateTimeField(auto_now=True)

    
    def get_absolute_url(self):
        return reverse("article_detail", kwargs={"slug": self.slug})

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)
    
    def __str__(self) -> str:
        return self.name
    