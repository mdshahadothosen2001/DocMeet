from django.shortcuts import get_object_or_404

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
        specialization_id = request.query_params.get("id")
        if specialization_id is None:
            specialization_id = request.query_params.get("specialization_id")
        doctor_id = request.query_params.get("doctor_id")

        if doctor_id:
            appointments =AppointmentModel.objects.filter(doctor=doctor_id, availability=True)
            serializer = AppointmentListSerializer(appointments, many=True)
            return Response(serializer.data, status=HTTP_200_OK)

        if specialization_id:
            doctor = get_object_or_404(Doctor, specialization=specialization_id)
            appointments =AppointmentModel.objects.filter(doctor=doctor.id, availability=True)
            serializer = AppointmentListSerializer(appointments, many=True)
            return Response(serializer.data, status=HTTP_200_OK)


        appointments =AppointmentModel.objects.filter(availability=True)
        serializer = AppointmentListSerializer(appointments, many=True)
        return Response(serializer.data, status=HTTP_200_OK)
