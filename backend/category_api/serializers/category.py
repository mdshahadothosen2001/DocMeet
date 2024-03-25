from rest_framework import serializers

from specialization.models import SpecializationModel


class SpecializationSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpecializationModel
        fields = ["id", "specialized_name", "image",]
