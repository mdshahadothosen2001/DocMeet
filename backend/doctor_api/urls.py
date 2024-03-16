from django.urls import path

from .views.token import MyTokenObtainPairView
from .views.profile import DoctorProfileView
from .views.profile_update import DoctorUpdateProfileView


urlpatterns = [
    # POST: localhost:8000/api/doctor/login/
    path(route="login/", view=MyTokenObtainPairView.as_view(), name="doctor_login"),
    # GET: localhost:8000/api/doctor/profile/
    path(route="profile/", view=DoctorProfileView.as_view(), name="doctor_profile"),
    # PATCH: localhost:8000/api/doctor/profile/update/
    path(route="profile/update/", view=DoctorUpdateProfileView.as_view(), name="doctor_profile_update"),
]
