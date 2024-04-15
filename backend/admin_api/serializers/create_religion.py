from rest_framework.serializers import ModelSerializer

from religion.models import ReligionModel


class CreateReligionSerializer(ModelSerializer):
    class Meta:
        model = ReligionModel
        fields = ["id", "name"]
