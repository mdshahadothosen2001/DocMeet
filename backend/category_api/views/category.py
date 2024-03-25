from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
from rest_framework.views import APIView

from specialization.models import SpecializationModel
from ..serializers.category import SpecializationSerializer


class SpecializationView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        specializations = SpecializationModel.objects.all()
        serializer = SpecializationSerializer(specializations, many=True)
        return Response(serializer.data, status=HTTP_200_OK)
