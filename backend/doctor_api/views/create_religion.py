from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from ..serializers.create_religion import CreateReligionSerializer
from utils.custom_permission import IsDoctor


class CreateReligionView(APIView):
    
    permission_classes = [IsDoctor]

    def validate_parameter(self, name):
        if name:
            return True
        else:
            return False
    
    def post(self, request, *args, **kwargs):
        name = request.data.get("name")
        if self.validate_parameter(name) is True:
            serializer = CreateReligionSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({"output":True, "message":"Successful in creating a religion."}, status=status.HTTP_201_CREATED)
            
        return Response({"output":False, "message":"Unsuccessful in creating a religion."}, status=status.HTTP_400_BAD_REQUEST)