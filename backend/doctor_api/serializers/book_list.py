from rest_framework import serializers

from book_appointment.models import BookAppointmentModel
from appointment.models import AppointmentModel
from user.models import UserAccount


class DoctorDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserAccount
        fields = [
            "id",
            "first_name", 
            "last_name", 
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

class PatientDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserAccount
        fields = [
            "id",
            "first_name",
            "last_name",
            "phone_number",
        ]
    
class BookAppointmentListSerializer(serializers.ModelSerializer):

    patient_detail = PatientDetailSerializer(source='patient', read_only=True)
    appointment_detail = AppointmentListSerializer(source='appointment', read_only=True)

    class Meta:
        model = BookAppointmentModel
        fields = [
            "id",
            "patient_detail",
            "appointment_detail",
            "is_complete", 
            ]
