import requests

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from django.shortcuts import get_object_or_404

from book_appointment.models import BookAppointmentModel
from utils.custom_permission import IsDoctor
from ..serializers.book_confirm import BookConfirmSerializer


class BookConfirmView(APIView):
    """User can update their profile information"""

    permission_classes = [IsDoctor]

    def validate_parameter(self, id):
        if id:
            return True
        else:
            return False
        
    def patch(self, request, *args, **kwargs):

        book_id = request.data.get("id")
        if self.validate_parameter(book_id) is True:
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
                    'subject': "Your Appointment Booking Confirmation",
                    'body': f"""We are pleased to inform you that your appointment has been successfully booked."
                                
                            Details of your appointment:
                            - Day: {appointment_day}
                            - Date: {appointment_date}
                            - Time: {appointment_time}
                            - Doctor: Dr. {doctor_first_name} {doctor_last_name}
                            - Location: DocMeet

                            If you have any questions or need to reschedule, please do not hesitate to contact us at [Contact Information].

                            Thank you for choosing our services. We look forward to seeing you.

                            Best regards,

                            [Your Clinic/Hospital Name]
                            [Your Contact Information]"""
                }
                email_sent = requests.post(api_url, data=payload)
            serializer =  BookConfirmSerializer(instance=book_instance, data={"is_complete":True})
            if serializer.is_valid():
                serializer.save()
                return Response({"output":True, "message":"Successful in confirming a book."}, status=status.HTTP_202_ACCEPTED)
            
        return Response({"output":False, "message":"Unsuccessful in confirming a book."}, status=status.HTTP_400_BAD_REQUEST)
