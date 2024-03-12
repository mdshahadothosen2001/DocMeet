from django.contrib import admin

from .models import BookAppointmentModel


class BookAppointmentAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "patient",
        "appointment",
        "is_complete",
    )
    list_display_links = ("is_complete",)
    search_fields = ("is_complete",)
    list_per_page = 25


admin.site.register(BookAppointmentModel, BookAppointmentAdmin)
