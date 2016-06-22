from .options import *
from django.db import models


class SocialNetwork(models.Model):
    name = models.CharField(max_length=140)
    title = models.CharField(max_length=140, blank=True)
    link = models.CharField(max_length=250, blank=True)
    slug = models.CharField(max_length=50)
    icon = models.CharField(max_length=25, choices=ICON_SOCIAL_NETWORK)
    color = models.CharField(max_length=7, blank=True)
    second_color = models.CharField(max_length=7, blank=True)
    klass = models.CharField(max_length=250, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Social network"
        verbose_name_plural = "Social networks"


class TypeLatter(models.Model):
    name = models.CharField(max_length=250)
    from_date = models.DateField()
    to_date = models.DateField()
    from_link = models.CharField(max_length=250, blank=True)
    comment = models.TextField(blank=True)
    description = models.TextField(blank=True)
    template = models.CharField(max_length=25, choices=TEMPLATE_FOR_EMAIL)
    viseble = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    def count_address(self):
        return Latter.objects.filter(type=self)

    class Meta:
        verbose_name = "Delivery"
        verbose_name_plural = "Mailing"


class Latter(models.Model):
    name = models.CharField(max_length=256, blank=True)
    email = models.EmailField(max_length=75)
    date_sub = models.DateField(blank=True)
    date_conf = models.DateField(blank=True)
    date_unsub = models.DateField(blank=True)
    ip = models. GenericIPAddressField()
    type = models.ManyToManyField(TypeLatter)

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = "Email addres"
        verbose_name_plural = "Emails address"
