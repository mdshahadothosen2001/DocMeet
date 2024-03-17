from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny

from user.models import Doctor
from ..serializers.doctor import DoctorListSerializer


class DoctorListView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        doctor = Doctor.objects.values()
        serializer = DoctorListSerializer(doctor, many=True)
        return Response(serializer.data, status=HTTP_200_OK)
