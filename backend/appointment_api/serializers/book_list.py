from rest_framework import serializers

from book_appointment.models import BookAppointmentModel
from user.models import UserAccount


class PatientDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserAccount
        fields = [
            "id",
            "first_name", 
        ]
    
class BookAppointmentListSerializer(serializers.ModelSerializer):

    patient_detail = PatientDetailSerializer(source='patient', read_only=True)

    class Meta:
        model = BookAppointmentModel
        fields = [
            "id",
            "patient_detail",
            "is_complete", 
            ]
