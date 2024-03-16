from django.urls import path

from .views.appointment import AppointmentListView



urlpatterns = [
    # GET: localhost:8000/api/appointment/list/
    path(route="list/", view=AppointmentListView.as_view(), name="appointment_list"),
]
