from django.shortcuts import get_list_or_404

from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny

from appointment.models import AppointmentModel

from ..serializers.appointment import AppointmentListSerializer


class AppointmentListView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        appointments =AppointmentModel.objects.all()
        serializer = AppointmentListSerializer(appointments, many=True)
        return Response(serializer.data, status=HTTP_200_OK)
