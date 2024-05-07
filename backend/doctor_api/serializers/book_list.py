from rest_framework import serializers
from book_appointment.models import BookAppointmentModel
from user.models import UserAccount

class BookAppointmentListSerializer(serializers.ModelSerializer):
    phone_number = serializers.CharField(source='patient.phone_number', read_only=True)
    email = serializers.CharField(source='patient.email', read_only=True)
    first_name = serializers.CharField(source='patient.first_name', read_only=True)
    last_name = serializers.CharField(source='patient.last_name', read_only=True)
    day = serializers.CharField(source='appointment.day', read_only=True)
    date = serializers.CharField(source='appointment.date', read_only=True)
    start_time = serializers.CharField(source='appointment.start_time', read_only=True)
    end_time = serializers.CharField(source='appointment.end_time', read_only=True)

    class Meta:
        model = BookAppointmentModel
        fields = ["id", "phone_number", "email", "first_name", "last_name", "day", "date", "start_time", "end_time", "is_complete"]
