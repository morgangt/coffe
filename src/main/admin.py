from django.contrib import admin
from . import models
from django_markdown.admin import MarkdownModelAdmin


class PostAdmin(MarkdownModelAdmin):
    list_display = ("title", "description", "created")
    prepopulated_fields = {"slug": ("title",)}


class TagAdmin(admin.ModelAdmin):
    list_display = ("name", "description", "slug")
    prepopulated_fields = {"slug": ("name",)}


class RubricAdmin(admin.ModelAdmin):
    list_display = ("name", "description", "slug")
    prepopulated_fields = {"slug": ("name",)}


admin.site.register(models.Post, PostAdmin)
admin.site.register(models.Tag, TagAdmin)
admin.site.register(models.Rubric, RubricAdmin)
