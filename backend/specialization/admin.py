from django.contrib import admin
from django.utils.html import format_html

from .models import SpecializationModel


class SpecializationAdmin(admin.ModelAdmin):
    def image_display(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="max-height: 200px; max-width: 200px;" />', obj.image.url)
        else:
            return "No Image"
    
    list_display = (
        "id",
        "specialized_name",
        "image_display",
    )
    list_display_links = ("specialized_name",)
    search_fields = ("specialized_name",)
    list_per_page = 25


admin.site.register(SpecializationModel, SpecializationAdmin)
