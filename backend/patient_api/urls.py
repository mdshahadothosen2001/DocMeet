from django.urls import path

from .views.token import MyTokenObtainPairView
from .views.register import UserRegistrationView
from .views.profile import PatientProfileView


urlpatterns = [
    # POST: localhost:8000/api/patient/register/
    path(route="register/", view=UserRegistrationView.as_view(), name="patient_register"),
    # POST: localhost:8000/api/patient/login/
    path(route="login/", view=MyTokenObtainPairView.as_view(), name="patient_login"),
    # GET: localhost:8000/api/patient/profile/
    path(route="profile/", view=PatientProfileView.as_view(), name="patient_profile"),
]
