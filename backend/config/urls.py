from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/patient/", include("patient_api.urls")),
    path("api/doctor/", include("doctor_api.urls")),
]
