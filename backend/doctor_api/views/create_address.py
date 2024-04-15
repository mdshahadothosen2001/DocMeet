from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from utils.custom_permission import IsDoctor
from utils.utils import tokenValidation
from ..serializers.create_address import CreateAddressSerializer, CreateUserAddressSerializer


class CreateAddressView(APIView):
    permission_classes = [IsDoctor]

    def post(self, request, *args, **kwargs):
        serializer = CreateAddressSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            payload = tokenValidation(request)
            user_data = {
                "user":payload.get("id"),
                "address":serializer.data.get("id")
            }
            user_address = CreateUserAddressSerializer(data=user_data)
            if user_address.is_valid():
                user_address.save()
                return Response({"output":True, "message":"Successful in creating a address."}, status=status.HTTP_201_CREATED)
        
        return Response({"output":False, "message":"UnSuccessful in creating a address."}, status=status.HTTP_400_BAD_REQUEST)
