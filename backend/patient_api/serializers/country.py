from rest_framework.serializers import ModelSerializer

from country.models import CountryModel


class CountryListSerializers(ModelSerializer):
    class Meta:
        model = CountryModel
        fields = ["id", "name"]
