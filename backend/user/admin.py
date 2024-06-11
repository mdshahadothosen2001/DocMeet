from django.contrib import admin
from django.utils.html import mark_safe

from user.models import Patient, UserAccount, Doctor


class UserAccountAdmin(admin.ModelAdmin):
    def display_picture(self, obj):
        return mark_safe('<img src="%s" style="max-width:100px; max-height:100px;" />' % obj.picture)
    display_picture.allow_tags = True
    display_picture.short_description = 'Picture'

    list_display = (
        "phone_number",
        "email",
        "user_type",
        "first_name",
        "last_name",
        "gender",
        "date_of_birth",
        "religion",
        "marital_status",
        "nationality",
        "emergency_contact",
        "display_picture",
        "is_active",
        "is_admin",
        "is_patient",
        "is_doctor",
        "is_staff",
        "is_superuser",
    )
    list_display_links = (
        "phone_number",
        "email",
        "first_name",
        "last_name",
        "display_picture",
    )
    search_fields = (
        "phone_number",
        "email",
    )
    list_per_page = 25


class PatientAdmin(admin.ModelAdmin):
    def display_picture(self, obj):
        return mark_safe('<img src="%s" style="max-width:100px; max-height:100px;" />' % obj.picture)
    display_picture.allow_tags = True
    display_picture.short_description = 'Picture'

    list_display = (
        "id",
        "phone_number",
        "email",
        "first_name",
        "last_name",
        "gender",
        "blood_group",
        "emergency_contact",
        "display_picture",
        "religion",
        "occupation",
        "is_patient",
        "is_active",
    )
    list_display_links = (
        "phone_number",
        "email",
    )
    search_fields = (
        "phone_number",
        "email",
    )
    list_per_page = 25


class DoctorAdmin(admin.ModelAdmin):
    def display_picture(self, obj):
        return mark_safe('<img src="%s" style="max-width:100px; max-height:100px;" />' % obj.picture)
    display_picture.allow_tags = True
    display_picture.short_description = 'Picture'
    
    list_display = (
        "id",
        "phone_number",
        "email",
        "first_name",
        "last_name",
        "specialization",
        "gender",
        "marital_status",
        "emergency_contact",
        "display_picture",
        "qualification",
        "is_doctor",
        "is_active",
    )
    list_display_links = (
        "phone_number",
        "email",
    )
    search_fields = (
        "phone_number",
        "email",
    )
    list_per_page = 25


admin.site.register(UserAccount, UserAccountAdmin)
admin.site.register(Patient, PatientAdmin)
admin.site.register(Doctor, DoctorAdmin)
