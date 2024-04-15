from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from utils.custom_permission import IsDoctor
from ..serializers.create_appointment import CreateAppointmentSerializer


class CreateAppointmentView(APIView):

    permission_classes = [IsDoctor]

    def validate_parameter(self, doctor, day, date, start_time, end_time):
        if doctor and day and date and start_time and end_time:
            return True
        else:
            return False
    
    def post(self, request, *args, **kwargs):
        doctor = request.data.get("doctor")
        day = request.data.get("day")
        date = request.data.get("date")
        start_time = request.data.get("start_time")
        end_time = request.data.get("end_time")
        if self.validate_parameter(doctor, day, date, start_time, end_time) is True:
            serializer = CreateAppointmentSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({"output":True, "message":"Successful in creating a appointment."}, status=status.HTTP_201_CREATED)
        return Response({"output":False, "message":"UnSuccessful in creating a appointment."}, status=status.HTTP_400_BAD_REQUEST)
