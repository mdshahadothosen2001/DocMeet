from rest_framework.serializers import ModelSerializer

from address.models import AddressModel
from user_address.models import UserAddressModel


class CreateAddressSerializer(ModelSerializer):
    class Meta:
        model = AddressModel
        fields = ["id", "unit_number", "street_number", "address_line1", "address_line2", "city", "region", "postal_code", "country"]

class CreateUserAddressSerializer(ModelSerializer):
    class Meta:
        model = UserAddressModel
        fields = ["user", "address", "is_default"]
