from django.db import models
from gallery.models import Image
from django.shortcuts import resolve_url
from django.utils.translation import ugettext_lazy as _
from solo.models import SingletonModel


class Tag(models.Model):
    name = models.CharField(max_length=140)
    slug = models.CharField(max_length=50)
    description = models.CharField(max_length=250)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Тэг"
        verbose_name_plural = "Тэги"


class Rubric(models.Model):
    name = models.CharField(max_length=140)
    slug = models.CharField(max_length=50)
    description = models.CharField(max_length=250)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Рубрика"
        verbose_name_plural = "Рубрики"


class PostQuerySet(models.QuerySet):
    def published(self):
        return self.filter(publish=True)


class Post(models.Model):
    image = models.ForeignKey(Image)
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=256)
    body = models.TextField()
    slug = models.SlugField(max_length=200, unique=True)
    tag = models.ManyToManyField(Tag)
    rubrica = models.ForeignKey(Rubric)
    publish = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    objects = PostQuerySet.as_manager()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Пост"
        verbose_name_plural = "Посты"
