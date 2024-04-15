from rest_framework import serializers

from book_appointment.models import BookAppointmentModel


class BookAppointmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = BookAppointmentModel
        fields = [
            "id",
            "patient",
            "appointment",
            "is_complete", 
        ]
    