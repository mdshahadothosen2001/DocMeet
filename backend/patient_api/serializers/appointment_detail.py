from rest_framework import serializers

from appointment.models import AppointmentModel
from user.models import UserAccount


class DoctorDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserAccount
        fields = [
            "id",
            "first_name",
            "last_name", 
            "gender",
            "qualification",
            "specialization",
            "picture",
        ]

class CustomTimeField(serializers.TimeField):
    def to_representation(self, value):
        if not value:
            return None
        return value.strftime('%I:%M %p')
    
class AppointmentListSerializer(serializers.ModelSerializer):

    doctor_detail = DoctorDetailSerializer(source='doctor', read_only=True)
    start_time = CustomTimeField()
    end_time = CustomTimeField()

    class Meta:
        model = AppointmentModel
        fields = [
            "id",
            "doctor_detail",
            "day", 
            "date", 
            "start_time",
            "end_time",
            "availability",
            ]
