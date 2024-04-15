from django.urls import path

from .views.token import MyTokenObtainPairView
from .views.profile import DoctorProfileView
from .views.profile_update import DoctorUpdateProfileView
from .views.register import UserRegistrationView
from .views.doctor import DoctorListView


urlpatterns = [
    # POST: localhost:8000/api/doctor/register/
    path(route="register/", view=UserRegistrationView.as_view(), name="doctor_register"),
    # POST: localhost:8000/api/doctor/login/
    path(route="login/", view=MyTokenObtainPairView.as_view(), name="doctor_login"),
    # GET: localhost:8000/api/doctor/profile/
    path(route="profile/", view=DoctorProfileView.as_view(), name="doctor_profile"),
    # PATCH: localhost:8000/api/doctor/profile/update/
    path(route="profile/update/", view=DoctorUpdateProfileView.as_view(), name="doctor_profile_update"),
    # GET: localhost:8000/api/doctor/list/
    path(route="list/", view=DoctorListView.as_view(), name="doctor_list"),
]
