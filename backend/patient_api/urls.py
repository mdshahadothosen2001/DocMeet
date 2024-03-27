from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

from .views.token import MyTokenObtainPairView
from .views.register import UserRegistrationView
from .views.profile import PatientProfileView
from .views.profile_update import PatientUpdateProfileView


urlpatterns = [
    # POST: localhost:8000/api/patient/register/
    path(route="register/", view=UserRegistrationView.as_view(), name="patient_register"),
    # POST: localhost:8000/api/patient/login/
    path(route="login/", view=MyTokenObtainPairView.as_view(), name="patient_login"),
    # GET: localhost:8000/api/patient/profile/
    path(route="profile/", view=PatientProfileView.as_view(), name="patient_profile"),
    # PATCH: localhost:8000/api/patient/profile/update/
    path(route="profile/update/", view=PatientUpdateProfileView.as_view(), name="patient_profile_update"),
    # POST: localhost:8000/api/patient/token/refresh/
    path(route="token/refresh/", view=TokenRefreshView.as_view(), name="token_refresh"),
]
