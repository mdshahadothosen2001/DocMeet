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
            "profile_picture",
        ]
    
class AppointmentListSerializer(serializers.ModelSerializer):

    doctor_detail = DoctorDetailSerializer(source='doctor', read_only=True)

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
