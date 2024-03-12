from django.contrib import admin

from .models import SpecializationModel


class SpecializationAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "specialized_name",
    )
    list_display_links = ("specialized_name",)
    search_fields = ("specialized_name",)
    list_per_page = 25


admin.site.register(SpecializationModel, SpecializationAdmin)
