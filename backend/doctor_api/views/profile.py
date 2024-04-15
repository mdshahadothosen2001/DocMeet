from django.shortcuts import get_object_or_404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from user.models import UserAccount
from utils.utils import tokenValidation
from utils.custom_permission import IsDoctor
from ..serializers.profile import DoctorProfileSerializer


class DoctorProfileView(APIView):
    permission_classes = [IsDoctor]

    def get(self, request):
        doctor = get_object_or_404(
            UserAccount, phone_number=tokenValidation(request)["phone_number"]
        )
        serializer = DoctorProfileSerializer(doctor)
        return Response(serializer.data, status=status.HTTP_200_OK)
