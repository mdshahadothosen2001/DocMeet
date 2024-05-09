from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from book_appointment.models import BookAppointmentModel
from utils.custom_permission import IsDoctor
from utils.utils import tokenValidation
from ..serializers.patient_list import PatienttListSerializer


class PatientListView(APIView):
    permission_classes = [IsDoctor]

    def get(self, request):
        doctor_id = tokenValidation(request)["id"]
        appointments = BookAppointmentModel.objects.filter(appointment__doctor=doctor_id, is_complete=True, is_active=False)
        serializer = PatienttListSerializer(appointments, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
