from rest_framework import serializers

from book_appointment.models import BookAppointmentModel


class BookConfirmSerializer(serializers.ModelSerializer):

    class Meta:
        model = BookAppointmentModel
        fields = [
            "id",
            "is_complete", 
        ]
    