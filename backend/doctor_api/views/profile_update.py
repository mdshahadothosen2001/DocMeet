from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST

from user.models import UserAccount
from utils.utils import tokenValidation

from ..serializers.profile_update import DoctorProfileUpdateSerializer


class DoctorUpdateProfileView(APIView):
    """User can update their profile information"""

    permission_classes = [IsAuthenticated]

    def patch(self, request, *args, **kwargs):

        payload = tokenValidation(request)
        email = payload.get("email")

        if email:
            doctor = UserAccount.objects.get(email=email)
            serializer = DoctorProfileUpdateSerializer(instance=doctor, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({"message": "successfully update your profile"}, status=HTTP_201_CREATED)
        return Response({"message": "Incomplete update process"}, status=HTTP_400_BAD_REQUEST)
