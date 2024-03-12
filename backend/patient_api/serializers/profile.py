from rest_framework import serializers

from user.models import UserAccount


class PatientProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserAccount
        fields = [
            "id", 
            "phone_number", 
            "email", "first_name", 
            "last_name", 
            "gender", 
            "blood_group", 
            "date_of_birth", 
            "religion", 
            "marital_status",
            ]
