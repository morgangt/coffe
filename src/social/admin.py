from django.contrib import admin
from .models import *


class SocialNetworkAdmin(admin.ModelAdmin):
    list_display = ("name", "title", "slug", "link")
    prepopulated_fields = {"slug": ("name",)}


class TypeLatterAdmin(admin.ModelAdmin):
    list_display = ("name", "from_date", "to_date", "viseble")


class LatterAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "ip")


admin.site.register(SocialNetwork, SocialNetworkAdmin)
admin.site.register(TypeLatter, TypeLatterAdmin)
admin.site.register(Latter, LatterAdmin)