from rest_framework import serializers

from user.models import UserAccount


class PatientProfileUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserAccount
        fields = [
            "id",
            "email",
            "first_name", 
            "last_name",
            "profile_picture",
            "picture",
            "emergency_contact", 
            "gender", 
            "blood_group", 
            "date_of_birth", 
            "religion", 
            "marital_status",
            "nationality", 
            "occupation",
            ]
