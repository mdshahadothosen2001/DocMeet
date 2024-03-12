from django.urls import path

from .views.token import MyTokenObtainPairView
from .views.register import UserRegistrationView


urlpatterns = [
    # POST: localhost:8000/api/patient/register/
    path(route="register/", view=UserRegistrationView.as_view(), name="token_obtain_pair"),
    # POST: localhost:8000/api/patient/login/
    path(route="login/", view=MyTokenObtainPairView.as_view(), name="token_obtain_pair"),
]
