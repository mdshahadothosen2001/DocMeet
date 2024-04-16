from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from ..serializers.religion import ReligionListSerializers
from religion.models import ReligionModel


class ReligionListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *agrs, **kwargs):
        religions = ReligionModel.objects.all()
        serializer = ReligionListSerializers(religions, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
