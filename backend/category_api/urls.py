from django.urls import path

from .views.category import SpecializationView

urlpatterns = [
    # GET: localhost:8000/api/specialization/list/
    path("list/", SpecializationView.as_view(), name="specializations"),
]
