from rest_framework.permissions import AllowAny
from rest_framework.generics import RetrieveAPIView

from appointment.models import AppointmentModel
from ..serializers.appointment_detail import AppointmentListSerializer


class AppointmentDetailView(RetrieveAPIView):
    permission_classes = [AllowAny]
    queryset = AppointmentModel
    serializer_class = AppointmentListSerializer
