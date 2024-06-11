from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny

from appointment.models import AppointmentModel
from ..serializers.appointment import AppointmentListSerializer


class AppointmentListView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        doctor_id = request.query_params.get("doctor_id")

        if doctor_id:
            appointments =AppointmentModel.objects.filter(doctor=doctor_id, availability=True)
            serializer = AppointmentListSerializer(appointments, many=True)
            return Response(serializer.data, status=HTTP_200_OK)

        appointments =AppointmentModel.objects.filter(availability=True)
        serializer = AppointmentListSerializer(appointments, many=True)
        return Response(serializer.data, status=HTTP_200_OK)


class AppointmentListWhichRecentCreatedView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        appointments =AppointmentModel.objects.filter(availability=True).order_by("created_at")[:5]
        serializer = AppointmentListSerializer(appointments, many=True)
        return Response(serializer.data, status=HTTP_200_OK)
