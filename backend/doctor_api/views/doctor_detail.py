from django.shortcuts import get_object_or_404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny

from user.models import Doctor


class DoctorDetailForPatient(APIView):
    permission_classes = [AllowAny]

    
    def validate_parameter(self, id):
        if id:
            return True
        else:
            return False
        
    def get(self, request, *agrs, **kwargs):
        id = request.query_params.get("id")
        if self.validate_parameter(id) is True:
            doctor = get_object_or_404(Doctor, id=id)
            doctor = {
                "name": doctor.first_name + " " + doctor.last_name,
                "email":doctor.email,
                "image":doctor.picture,
                "specialization":doctor.specialization.name,
                "qualification":doctor.qualification,
            }
            return Response(doctor, status=status.HTTP_200_OK)
        
        return Response({"output":False, "message":"Incompleted process, please provide valid doctor id"}, status=status.HTTP_400_BAD_REQUEST)
