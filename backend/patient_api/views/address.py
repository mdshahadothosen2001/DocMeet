from django.shortcuts import get_list_or_404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from ..serializers.address import AddressSerializer, UserAddressSerializer
from user_address.models import UserAddressModel
from utils.utils import tokenValidation


class AddressView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        user_id=tokenValidation(request)
        addresses = get_list_or_404(UserAddressModel, user=user_id.get("id"))
        serializer = UserAddressSerializer(addresses, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
