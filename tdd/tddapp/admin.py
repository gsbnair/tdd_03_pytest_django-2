from django.contrib import admin

# Register your models here.
from . import models

# Register your models here.


class PostAdmin(admin.ModelAdmin):
    model = models.Post
    list_display = ("excerpt",)

    def excerpt(self, obj):
        return obj.get_excerpt(5)