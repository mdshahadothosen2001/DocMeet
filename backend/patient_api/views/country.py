from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from ..serializers.country import CountryListSerializers
from country.models import CountryModel

class CountryListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        countries = CountryModel.objects.all()
        serializer = CountryListSerializers(countries, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
