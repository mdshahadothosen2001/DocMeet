from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

from .views.register import UserRegistrationView
from .views.token import CustomTokenObtainPairView
from .views.create_religion import CreateReligionView
from .views.create_specialization import CreateSpecializationView
from .views.create_appointment import CreateAppointmentView
from .views.doctor import DoctorListView
from .views.profile import DoctorProfileView
from .views.book_list import BookAppointmentListView
from .views.book_confirm import BookConfirmView
from .views.book_delete import BookDeleteView
from .views.profile_update import DoctorUpdateProfileView
from .views.create_address import CreateAddressView



urlpatterns = [
    # POST: localhost:8000/api/doctor/register/
    path(route="register/", view=UserRegistrationView.as_view(), name="doctor_register"),
    # POST: localhost:8000/api/doctor/login/
    path(route="login/", view=CustomTokenObtainPairView.as_view(), name="doctor_login"),
    # POST: localhost:8000/api/doctor/login/refresh/
    path(route="login/refresh/", view=TokenRefreshView.as_view(), name="doctor_login_refresh"),
    # GET: localhost:8000/api/doctor/profile/
    path(route="profile/", view=DoctorProfileView.as_view(), name="doctor_profile"),
    # PATCH: localhost:8000/api/doctor/profile/update/
    path(route="profile/update/", view=DoctorUpdateProfileView.as_view(), name="doctor_profile_update"),
    # GET: localhost:8000/api/doctor/list/
    path(route="list/", view=DoctorListView.as_view(), name="doctor_list"),
    # POST: localhost:8000/api/doctor/religion/create/
    path(route="religion/create/", view=CreateReligionView.as_view(), name="religion_create"),
    # POST: localhost:8000/api/doctor/specialized/create/
    path(route="specialization/create/", view=CreateSpecializationView.as_view(), name="specialization_create"),
    # POST: localhost:8000/api/doctor/appointment-create/
    path(route="appointment-create/", view=CreateAppointmentView.as_view(), name="appointment_create"),
    # GET: localhost:8000/api/doctor/book-list/
    path(route="book-list/", view=BookAppointmentListView.as_view(), name="book_list"),
    # PATCH: localhost:8000/api/doctor/book-confirm/
    path(route="book-confirm/", view=BookConfirmView.as_view(), name="book_confirm"),
    # DELETE: localhost:8000/api/doctor/book-delete/1/
    path(route="book-delete/<int:pk>/", view=BookDeleteView.as_view(), name="book_delete"),
    # POST: localhost:8000/api/doctor/address-create/
    path(route="address-create/", view=CreateAddressView.as_view(), name="address_create"),
]
