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
        doctor =  tokenValidation(request)["id"]
        patients =BookAppointmentModel.objects.filter(appointment__doctor=doctor, is_complete=True)
        
        serializer = PatienttListSerializer(patients, many=True)
        unique_patients = self.get_unique_patients(serializer.data)
        return Response(unique_patients, status=status.HTTP_200_OK)
    
    def get_unique_patients(self, data):
        unique_ids = set()
        unique_data = []
        
        for patient in data:
            patient_data = dict(patient)
            if patient_data["patient"]['id'] not in unique_ids:
                unique_data.append(patient_data)
                unique_ids.add(patient_data["patient"]['id'])
        
        return unique_data
