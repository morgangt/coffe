from django.db import models
from .options import TYPE_ALBOM


class Album(models.Model):
    name = models.CharField(max_length=140)
    description = models.CharField(max_length=256, blank=True)
    type = models.CharField(max_length=50, choices=TYPE_ALBOM)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Album"
        verbose_name_plural = "Albums"


class Image(models.Model):
    name = models.CharField(max_length=50)
    title = models.CharField(max_length=250, blank=True)
    description = models.CharField(max_length=256, blank=True)
    albom = models.ManyToManyField(Album, blank=True)
    pic = models.ImageField(upload_to='storage/img/standart', blank=True)
    mini_pic = models.ImageField(upload_to='storage/img/mini', blank=True)
    orig_pic = models.ImageField(upload_to='storage/img/origenal', blank=True)
    date = models.DateField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"


class Slider(models.Model):
    name = models.CharField(max_length=50)
    title = models.CharField(max_length=250, blank=True)
    image = models.ManyToManyField(Image)
    description = models.CharField(max_length=256, blank=True)
    link = models.CharField(max_length=256, blank=True)
    promo_pix = models.CharField(max_length=256, blank=True)
    code = models.TextField(blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Slider"
        verbose_name_plural = "Sliders"

