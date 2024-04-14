from rest_framework.serializers import ModelSerializer

from specialization.models import SpecializationModel


class CreateSpecializationSerializer(ModelSerializer):
    class Meta:
        model = SpecializationModel
        fields = ["id", "specialized_name", "picture"]
