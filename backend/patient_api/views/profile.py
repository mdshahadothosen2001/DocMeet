from django.shortcuts import get_object_or_404

from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

from user.models import UserAccount
from utils.utils import tokenValidation

from ..serializers.profile import PatientProfileSerializer


class PatientProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        patient = get_object_or_404(
            UserAccount, phone_number=tokenValidation(request)["phone_number"]
        )
        serializer = PatientProfileSerializer(patient)
        return Response(serializer.data, status=HTTP_200_OK)
