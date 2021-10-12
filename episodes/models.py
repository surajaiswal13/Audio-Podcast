from django.db import models
from shows.models import Show
from django.utils.text import slugify

# Create your models here.

class Episode(models.Model):

    title = models.CharField(max_length=256,unique=True)
    slug = models.SlugField(allow_unicode=True,unique=True, blank=True)
    description = models.TextField(blank=True,default='')
    image = models.ImageField(blank=True, upload_to="episode_images")
    audio = models.FileField(blank=True, upload_to="episode_audios")
    show = models.ForeignKey(Show, related_name="episodes", on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def save(self,*args,**kwargs):
        self.slug=slugify(self.title)
        super().save(*args,**kwargs)