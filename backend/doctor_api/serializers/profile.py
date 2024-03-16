from rest_framework import serializers

from user.models import UserAccount


class DoctorProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserAccount
        fields = [
            "id",
            "email",
            "first_name", 
            "last_name", 
            "gender",
            "qualification",
            "specialization",
            ]
