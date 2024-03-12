from django.urls import path

from .views.token import MyTokenObtainPairView


urlpatterns = [
    # POST: localhost:8000/api/patient/login/
    path(route="login/", view=MyTokenObtainPairView.as_view(), name="token_obtain_pair"),
]
