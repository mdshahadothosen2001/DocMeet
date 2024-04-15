from django.urls import path

from .views.create_religion import CreateReligionView
from .views.create_specialization import CreateSpecializationView


urlpatterns = [
    # POST: localhost:8000/api/admin/religion/create/
    path(route="religion/create/", view=CreateReligionView.as_view(), name="admin_religion_create"),
    # POST: localhost:8000/api/admin/specialized/create/
    path(route="specialization/create/", view=CreateSpecializationView.as_view(), name="admin_specialization_create"),
]
