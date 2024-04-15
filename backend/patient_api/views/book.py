from rest_framework.status import HTTP_202_ACCEPTED, HTTP_400_BAD_REQUEST
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from ..serializers.book import BookAppointmentSerializer
from book_appointment.models import BookAppointmentModel
from utils.custom_permission import IsPatient


class BookAppointmentView(APIView):
    """User can book any appointment."""

    permission_classes = [IsPatient]

    def validate_parameter(self, patient_id, appointment_id):
        if patient_id and appointment_id:
            return True
        else:
            return False

    def post(self, request, *args, **kwargs):
        patient_id = request.user.id
        appointment_id = request.data.get("id")

        if self.validate_parameter(patient_id, appointment_id) is True:
            book_instance = BookAppointmentModel.objects.filter(appointment=appointment_id).exists()
            if book_instance is False:
                book_appointment = {
                    "patient": patient_id,
                    "appointment": appointment_id,
                }

                serializer = BookAppointmentSerializer(data=book_appointment)
                if serializer.is_valid():
                    serializer.save()

                    return Response({"message":"Send your appointment request!"}, status=HTTP_202_ACCEPTED)

        return Response({"message":"Incompleted request! Please provide valid data"}, status=HTTP_400_BAD_REQUEST)
