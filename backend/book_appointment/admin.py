from django.contrib import admin

from .models import BookAppointmentModel


class BookAppointmentAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "patient",
        "appointment",
        "is_complete",
        "is_active",
    )
    list_display_links = (
        "patient",
        "appointment",
        "is_complete",
    )
    search_fields = ("is_complete", "is_active",)
    list_per_page = 25


admin.site.register(BookAppointmentModel, BookAppointmentAdmin)
