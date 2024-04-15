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
            return id.isdigit()
        else:
            return False
        
    def patch(self, request, *args, **kwargs):

        book_id = request.query_params.get("id")
        if self.validate_parameter(book_id) is True:
            book_instance = get_object_or_404(BookAppointmentModel, id=book_id)
            serializer =  BookConfirmSerializer(instance=book_instance, data={"is_complete":True})
            if serializer.is_valid():
                serializer.save()
                return Response({"output":True, "message":"Successful in confirming a book."}, status=status.HTTP_202_ACCEPTED)
            
        return Response({"output":False, "message":"Unsuccessful in confirming a book."}, status=status.HTTP_400_BAD_REQUEST)
