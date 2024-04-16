from django.urls import path

from rest_framework_simplejwt.views import TokenRefreshView

from .views.token import MyTokenObtainPairView
from .views.register import UserRegistrationView
from .views.profile import PatientProfileView
from .views.profile_update import PatientUpdateProfileView
from .views.doctor_list import DoctorListView
from .views.specialization import SpecializationView
from .views.appointment import AppointmentListView
from .views.book import BookAppointmentView
from .views.create_address import CreateAddressView
from .views.address import AddressView


urlpatterns = [
    # POST: localhost:8000/api/patient/register/
    path(route="register/", view=UserRegistrationView.as_view(), name="patient_register"),
    # POST: localhost:8000/api/patient/login/
    path(route="login/", view=MyTokenObtainPairView.as_view(), name="patient_login"),
    # POST: localhost:8000/api/patient/login/refresh/
    path(route="login/refresh/", view=TokenRefreshView.as_view(), name="login_refresh"),
    # GET: localhost:8000/api/patient/profile/
    path(route="profile/", view=PatientProfileView.as_view(), name="patient_profile"),
    # PATCH: localhost:8000/api/patient/profile/update/
    path(route="profile/update/", view=PatientUpdateProfileView.as_view(), name="patient_profile_update"),
    # GET: localhost:8000/api/patient/doctor-list/
    path(route="doctor-list/", view=DoctorListView.as_view(), name="doctor_list"),
    # GET: localhost:8000/api/patient/specialization-list/
    path("specialization-list/", SpecializationView.as_view(), name="specializations"),
    # GET: localhost:8000/api/patient/appointment-list/
    path(route="appointment-list/", view=AppointmentListView.as_view(), name="appointment_list"),
    # POST: localhost:8000/api/patient/appointment-book/
    path(route="appointment-book/", view=BookAppointmentView.as_view(), name="appointment_book"),
    # POST: localhost:8000/api/patient/address-create/
    path(route="address-create/", view=CreateAddressView.as_view(), name="address_create"),
    # GET: localhost:8000/api/patient/address/
    path(route="address/", view=AddressView.as_view(), name="patient_address"),
]
