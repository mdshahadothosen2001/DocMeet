from rest_framework.status import HTTP_202_ACCEPTED, HTTP_304_NOT_MODIFIED
from rest_framework.response import Response
from rest_framework.views import APIView

from django.shortcuts import get_object_or_404

from book_appointment.models import BookAppointmentModel
from utils.custom_permission import IsDoctor
from ..serializers.book_confirm import BookAppointmentConfirmSerializer


class BookConfirmView(APIView):
    """User can update their profile information"""

    permission_classes = [IsDoctor]

    def patch(self, request, *args, **kwargs):

        book_id = request.data.get("id")
        if book_id:
            book_instance = get_object_or_404(BookAppointmentModel, id=book_id)
            serializer =  BookAppointmentConfirmSerializer(instance=book_instance, data={"is_complete":True})
            if serializer.is_valid():
                serializer.save()
                return Response({"message": "successfully accepted book request"}, status=HTTP_202_ACCEPTED)

        return Response({"message": "Incomplete book request process"}, status=HTTP_304_NOT_MODIFIED)
