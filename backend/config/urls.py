from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/patient/", include("patient_api.urls")),
    path("api/doctor/", include("doctor_api.urls")),
    path("api/appointment/", include("appointment_api.urls")),
    path("api/specialization/", include("category_api.urls")),
    path("api/admin/", include("admin_api.urls")),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += [
        path("__debug__/", include("debug_toolbar.urls")),
    ]