from rest_framework import serializers
from book_appointment.models import BookAppointmentModel


class PatienttListSerializer(serializers.ModelSerializer):
    patient_id = serializers.CharField(source='patient.id', read_only=True)
    phone_number = serializers.CharField(source='patient.phone_number', read_only=True)
    email = serializers.CharField(source='patient.email', read_only=True)
    first_name = serializers.CharField(source='patient.first_name', read_only=True)
    last_name = serializers.CharField(source='patient.last_name', read_only=True)
    gender = serializers.CharField(source='patient.gender', read_only=True)
    marital_status = serializers.CharField(source='patient.marital_status', read_only=True)
    date_of_birth = serializers.CharField(source='patient.date_of_birth', read_only=True)
    blood_group = serializers.CharField(source='patient.blood_group', read_only=True)
    emergency_contact = serializers.CharField(source='patient.emergency_contact', read_only=True)

    class Meta:
        model = BookAppointmentModel
        fields = [
            "patient_id",
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
