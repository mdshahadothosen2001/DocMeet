from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny

from appointment.models import AppointmentModel
from user.models import Doctor
from ..serializers.appointment import AppointmentListSerializer


class AppointmentListView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        specialized_id = request.query_params.get("id")
        doctors = Doctor.objects.values()
        if specialized_id:
            doctors = doctors.filter(specialization=specialized_id)
            appointment_list = []
            for doctor in doctors:
                appointments =AppointmentModel.objects.filter(doctor=doctor.get("id"))
                serializer = AppointmentListSerializer(appointments, many=True)
                appointment_list += serializer.data
            return Response(appointment_list, status=HTTP_200_OK)


        appointments =AppointmentModel.objects.all()
        serializer = AppointmentListSerializer(appointments, many=True)
        return Response(serializer.data, status=HTTP_200_OK)
