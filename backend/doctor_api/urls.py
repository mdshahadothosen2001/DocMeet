from django.urls import path

from .views.token import MyTokenObtainPairView


urlpatterns = [
    # POST: localhost:8000/api/doctor/login/
    path(route="login/", view=MyTokenObtainPairView.as_view(), name="doctor_login"),
]
