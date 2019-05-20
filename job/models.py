from django.db import models
from job_doan.utils import get_unique_slug
from djangotoolbox.fields import ListField

# Create your models here.
class DichVu(models.Model):
    created_on = models.DateTimeField(auto_now_add=True, null=True)
    title = models.CharField(max_length=255,default='')
    slug = models.SlugField(max_length=255)
    text = models.TextField(default='')
    img = models.ImageField(null=True)


    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = get_unique_slug(self, 'title', 'slug')
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

class LinhVuc(models.Model):
    created_on = models.DateTimeField(auto_now_add=True, null=True)
    title = models.CharField(max_length=255,default='')
    slug = models.SlugField(max_length=255)
    text = models.TextField(default='')
    #img = models.ImageField(null=True)

    def __str__(self):
        return self.title

class ThanhPho(models.Model):
    created_on = models.DateTimeField(auto_now_add=True, null=True)
    title = models.CharField(max_length=255,default='')
    slug = models.SlugField(max_length=255)

    def __str__(self):
        return self.title


class ViecTheoDuAn(models.Model):
    created_on = models.DateTimeField(auto_now_add=True, null=True)
    title = models.CharField(max_length=255,default='')
    slug = models.SlugField(max_length=255)
    infojob = models.TextField(max_length=500, default='')
    file = models.FileField(default='')
    skill = models.CharField(max_length=255,default='')
    time_ex = models.DateTimeField(default='')
    ngansach = models.FloatField(max_length=255,default='')
    hinh = models.ImageField(default='')
    def __str__(self):
        return self.title
