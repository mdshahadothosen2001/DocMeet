from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

from user.models import UserAccount
from utils.utils import tokenValidation

from ..serializers.profile_update import PatientProfileUpdateSerializer


class PatientUpdateProfileView(APIView):
    """User can update their profile information"""

    permission_classes = [IsAuthenticated]

    def patch(self, request, *args, **kwargs):

        payload = tokenValidation(request)
        email = payload.get("email")

        if email:
            patient = UserAccount.objects.get(email=email)
            serializer = PatientProfileUpdateSerializer(instance=patient, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({"message": "successfully update your profile"})
        return Response({"message": "Incomplete update process"})
