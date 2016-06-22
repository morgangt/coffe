from django.contrib import admin
from .models import Album, Image, Slider


class AlbumAdmin(admin.ModelAdmin):
    list_display = ("name", "description", "type")


class ImageAdmin(admin.ModelAdmin):
    list_display = ("name", "title", "date")


class SliderAdmin(admin.ModelAdmin):
    list_display = ("name", "title", "link")


admin.site.register(Album, AlbumAdmin)
admin.site.register(Image, ImageAdmin)
admin.site.register(Slider, SliderAdmin)