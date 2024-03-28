from django.contrib import admin

from user.models import Patient, UserAccount, Doctor


class UserAccountAdmin(admin.ModelAdmin):
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
        "profile_image",
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
        "profile_image",
    )
    search_fields = (
        "phone_number",
        "email",
    )
    list_per_page = 25


class PatientAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "phone_number",
        "email",
        "first_name",
        "last_name",
        "gender",
        "blood_group",
        "emergency_contact",
        "profile_image",
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
    list_display = (
        "id",
        "phone_number",
        "email",
        "first_name",
        "last_name",
        "gender",
        "marital_status",
        "emergency_contact",
        "profile_image",
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
