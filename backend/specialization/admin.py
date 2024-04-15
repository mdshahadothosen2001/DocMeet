from django.contrib import admin
from django.utils.html import mark_safe

from .models import SpecializationModel


class SpecializationAdmin(admin.ModelAdmin):
    def display_picture(self, obj):
        return mark_safe('<img src="%s" style="max-width:100px; max-height:100px;" />' % obj.picture)
    display_picture.allow_tags = True
    display_picture.short_description = 'Picture'
    
    list_display = (
        "id",
        "name",
        "display_picture",
    )
    list_display_links = ("name",)
    search_fields = ("name",)
    list_per_page = 25


admin.site.register(SpecializationModel, SpecializationAdmin)
