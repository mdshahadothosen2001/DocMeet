from django.urls import path

from .views.appointment import AppointmentListView
from .views.book import BookAppointmentView
from .views.book_list import BookAppointmentListView
from .views.book_confirm import BookConfirmView


urlpatterns = [
    # GET: localhost:8000/api/appointment/list/
    path(route="list/", view=AppointmentListView.as_view(), name="appointment_list"),
    # POST: localhost:8000/api/appointment/book/
    path(route="book/", view=BookAppointmentView.as_view(), name="appointment_book"),
    # GET: localhost:8000/api/appointment/book/list/
    path(route="book/list/", view=BookAppointmentListView.as_view(), name="appointment_book_list"),
    # PATCH: localhost:8000/api/appointment/book/confirm/
    path(route="book/confirm/", view=BookConfirmView.as_view(), name="appointment_book_confirm"),
]
