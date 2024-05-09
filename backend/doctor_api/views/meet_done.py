from django.shortcuts import get_object_or_404

from rest_framework.views import APIView
from rest_framework.response import Response

from book_appointment.models import BookAppointmentModel
from utils.custom_permission import IsDoctor


class DoctorMeetView(APIView):
    permission_classes = [IsDoctor]

    def validate_parameter(self, id):
        return id is not None
        
    def patch(self, request, *args, **kwargs):

        book_id = request.data.get("id")
        if self.validate_parameter(book_id) is True:
            book_instance = get_object_or_404(BookAppointmentModel, id=book_id)
            book_instance.is_active = False
            book_instance.save()
            return Response("Successful in Doctor Meet a book.")
            
        return Response("Unsuccessful in Doctor Meet a book.")
