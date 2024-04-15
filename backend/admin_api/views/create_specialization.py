from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from utils.custom_permission import IsDoctor
from ..serializers.create_specialization import CreateSpecializationSerializer


class CreateSpecializationView(APIView):
    
    permission_classes = [IsDoctor]

    def post(self, request, *args, **kwargs):
        serializer = CreateSpecializationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"output":True, "message":"Successfully created specialized"}, status=status.HTTP_201_CREATED)
        return Response({"output":False, "message":"Unuccessfully created appointment"}, status=status.HTTP_400_BAD_REQUEST)
