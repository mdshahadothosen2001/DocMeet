from rest_framework import serializers

from user.models import UserAccount


class DoctorListSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserAccount
        fields = [
            "id",
            "first_name", 
            "last_name", 
            "qualification",
            "specialization",
            ]
