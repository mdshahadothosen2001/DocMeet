from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from utils.custom_permission import IsDoctor
from ..serializers.create_specialization import CreateSpecializationSerializer


class CreateSpecializationView(APIView):
    
    permission_classes = [IsDoctor]

    def validate_parameter(self, name, picture):
        if name and picture:
            return True
        else:
            return False

    def post(self, request, *args, **kwargs):
        name = request.data.get("name")
        picture = request.data.get("picture")
        if self.validate_parameter(name, picture) is True:
            serializer = CreateSpecializationSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({"output":True, "message":"Successful in creating a specialization."}, status=status.HTTP_201_CREATED)
            
        return Response({"output":False, "message":"Unsuccessful in creating a specialization."}, status=status.HTTP_400_BAD_REQUEST)
