from django.contrib import admin

from .models import AppointmentModel


class AppointmentAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "doctor",
        "day",
        "start_time",
        "end_time",
        "availability",
        "created_at",
        "updated_at",
    )
    list_display_links = ("doctor",
        "day",
        "start_time",
        "end_time",
        "availability",
        )
    search_fields = ("doctor",
        "day",
        "start_time",
        "end_time",
        "availability",
        )
    list_per_page = 25


admin.site.register(AppointmentModel, AppointmentAdmin)
