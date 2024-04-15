from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from utils.custom_permission import IsDoctor
from ..serializers.create_country import CreateCountrySerializer


class CreateCountryView(APIView):
    permission_classes = [IsDoctor]

    def post(self, request, *args, **kwargs):
        serializer = CreateCountrySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"output":True, "message":"Successful in creating a country."}, status=status.HTTP_201_CREATED)
        
        return Response({"output":False, "message":"UnSuccessful in creating a country."}, status=status.HTTP_400_BAD_REQUEST)
