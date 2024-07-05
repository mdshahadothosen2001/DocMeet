import requests

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

            patient_email = book_instance.patient.email
            if patient_email:
                appointment_day = book_instance.appointment.day
                appointment_date = book_instance.appointment.date
                appointment_time = book_instance.appointment.start_time
                doctor_first_name = book_instance.appointment.doctor.first_name
                doctor_last_name = book_instance.appointment.doctor.last_name
                api_url = "https://yourmailsender.pythonanywhere.com/send/mail/"
                payload = {
                    'email': patient_email,
                    'subject': "Your Appointment has been canceled",
                    'body': f"""You can choise any other slots of your respective doctor.
                                Thank you so much"""
                }
                email_sent = requests.post(api_url, data=payload)
            
            appointment_id = book_instance.appointment.id
            book_instance.delete()
            
            appointment_instance = AppointmentModel.objects.get(id=appointment_id)
            appointment_instance.availability = True
            appointment_instance.save()
            
            return Response("Successful in deleting a book.")
        
        return Response("Unsuccessful in deleting a book.")
