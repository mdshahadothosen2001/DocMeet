from rest_framework.serializers import ModelSerializer

from user_address.models import UserAddressModel
from address.models import AddressModel


class AddressSerializer(ModelSerializer):
    class Meta:
        model = AddressModel
        fields = ["id", "unit_number", "street_number", "address_line1", "address_line2", "city", "region", "postal_code", "country",]
    
class UserAddressSerializer(ModelSerializer):
    address = AddressSerializer()
    class Meta:
        model = UserAddressModel
        fields = ["id", "address", "is_default",]
