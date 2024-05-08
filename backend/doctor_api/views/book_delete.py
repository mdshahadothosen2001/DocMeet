
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from book_appointment.models import BookAppointmentModel
from appointment.models import AppointmentModel
from utils.custom_permission import IsDoctor

class BookDeleteView(APIView):
    """User can delete book appointment"""

    permission_classes = [IsDoctor]

    def validate_parameter(self, id):
        return id is not None

    def delete(self, request, *args, **kwargs):
        book_id = kwargs.get("pk")
        if self.validate_parameter(book_id):
            book_instance = get_object_or_404(BookAppointmentModel, id=book_id)
            
            appointment_id = book_instance.appointment.id
            book_instance.delete()
            
            appointment_instance = AppointmentModel.objects.get(id=appointment_id)
            appointment_instance.availability = True
            appointment_instance.save()
            
            return Response("Successful in deleting a book.")
        
        return Response("Unsuccessful in deleting a book.")
