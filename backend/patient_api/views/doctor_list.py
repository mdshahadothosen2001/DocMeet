from django.shortcuts import get_object_or_404

from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny

from user.models import Doctor
from specialization.models import SpecializationModel
from ..serializers.doctor_list import DoctorListSerializer


class DoctorListView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        specialized_id = request.query_params.get("specialization_id")
        doctors = Doctor.objects.values()
        if specialized_id:
            doctors = doctors.filter(specialization=specialized_id)
        serializer = DoctorListSerializer(doctors, many=True)
        return Response(serializer.data, status=HTTP_200_OK)
