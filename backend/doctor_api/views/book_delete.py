from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


from django.shortcuts import get_object_or_404

from book_appointment.models import BookAppointmentModel
from utils.custom_permission import IsDoctor


class BookDeleteView(APIView):
    """User can delete book appointment"""

    permission_classes = [IsDoctor]

    def validate_parameter(self, id):
        if id:
            return True
        else:
            return False
    
    def delete(self, request, *args, **kwargs):
        book_id = kwargs.get("pk")
        if self.validate_parameter(book_id) is True:
            book_instance = get_object_or_404(BookAppointmentModel, id=book_id)
            book_instance.delete()
            return Response({"output":True, "message":"Successful in deleting a book."}, status=status.HTTP_200_OK)

        return Response({"output":False, "message":"Unsuccessful in deleting a book."}, status=status.HTTP_400_BAD_REQUEST)
