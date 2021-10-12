from django.db import models
from django.utils.text import slugify

# Create your models here.


class Show(models.Model):
    title = models.CharField(max_length=256,unique=True)
    slug = models.SlugField(allow_unicode=True,unique=True, blank=True) # Change Name 
    description = models.TextField(blank=True,default='')
    image = models.ImageField(blank=True, upload_to="show_images") 

    def __str__(self):
        return self.title

    def save(self,*args,**kwargs):
        self.slug=slugify(self.title)
        super().save(*args,**kwargs)