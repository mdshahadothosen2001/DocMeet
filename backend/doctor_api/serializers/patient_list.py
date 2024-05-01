from rest_framework import serializers
from book_appointment.models import BookAppointmentModel
from user.models import UserAccount

class PatientDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAccount
        fields = [
            "id",
            "first_name",
            "last_name",
            "phone_number",
            "email",
            "gender",
            "marital_status",
            "date_of_birth",
            "blood_group",
            "emergency_contact",
        ]

class PatienttListSerializer(serializers.ModelSerializer):
    patient = PatientDetailSerializer(read_only=True)

    class Meta:
        model = BookAppointmentModel
        fields = [
            "patient",
        ]
