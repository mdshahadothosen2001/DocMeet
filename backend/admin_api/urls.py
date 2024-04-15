from django.urls import path

from .views.create_religion import CreateReligionView


urlpatterns = [
    # POST: localhost:8000/api/admin/religion/create/
    path(route="religion/create/", view=CreateReligionView.as_view(), name="admin_religion_create"),
]
