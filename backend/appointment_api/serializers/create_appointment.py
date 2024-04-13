from rest_framework.serializers import ModelSerializer

from appointment.models import AppointmentModel


class CreateAppointmentSerializer(ModelSerializer):
    class Meta:
        model = AppointmentModel
        fields = ["id", "doctor", "day", "date", "start_time", "end_time"]
