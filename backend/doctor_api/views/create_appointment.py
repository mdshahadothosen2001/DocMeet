from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from utils.custom_permission import IsDoctor
from utils.utils import tokenValidation
from ..serializers.create_appointment import CreateAppointmentSerializer


class CreateAppointmentView(APIView):

    permission_classes = [IsDoctor]

    def validate_parameter(self,day, date, start_time, end_time):
        if day and date and start_time and end_time:
            return True
        else:
            return False
    
    def post(self, request, *args, **kwargs):
        day = request.data.get("day")
        date = request.data.get("date")
        start_time = request.data.get("start_time")
        end_time = request.data.get("end_time")
        if self.validate_parameter(day, date, start_time, end_time) is True:
            doctor =  tokenValidation(request)["id"]
            appointment_data = {
                "doctor": doctor,
                "day": day,
                "date": date,
                "start_time": start_time,
                "end_time": end_time,
            }

            serializer = CreateAppointmentSerializer(data=appointment_data)
            if serializer.is_valid():
                serializer.save()
                return Response({"output":True, "message":"Successful in creating a appointment."}, status=status.HTTP_201_CREATED)
            
        return Response({"output":False, "message":"UnSuccessful in creating a appointment."}, status=status.HTTP_400_BAD_REQUEST)
