from rest_framework import serializers

from user.models import UserAccount
from specialization.models import SpecializationModel


class SpecializationSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpecializationModel
        fields = ["specialized_name"]

class DoctorListSerializer(serializers.ModelSerializer):
    specialization = serializers.SerializerMethodField()

    class Meta:
        model = UserAccount
        fields = [
            "id",
            "first_name", 
            "last_name", 
            "qualification",
            "specialization",
        ]

    def get_specialization(self, obj):
        if isinstance(obj, dict):
            specialization_id = obj.get('specialization_id')
            if specialization_id:
                specialization = SpecializationModel.objects.get(id=specialization_id)
                if specialization:
                    return SpecializationSerializer(specialization).data
        return None
