from django.urls import path

from .views.token import MyTokenObtainPairView
from .views.profile import DoctorProfileView


urlpatterns = [
    # POST: localhost:8000/api/doctor/login/
    path(route="login/", view=MyTokenObtainPairView.as_view(), name="doctor_login"),
    # GET: localhost:8000/api/doctor/profile/
    path(route="profile/", view=DoctorProfileView.as_view(), name="doctor_profile"),
]
