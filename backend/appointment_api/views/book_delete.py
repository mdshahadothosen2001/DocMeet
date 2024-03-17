from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.response import Response
from rest_framework.views import APIView

from book_appointment.models import BookAppointmentModel
from utils.custom_permission import IsDoctor


class BookDeleteView(APIView):
    """User can delete book appointment"""

    permission_classes = [IsDoctor]

    def delete(self, request, *args, **kwargs):
        book_id = kwargs.get("pk")
        if book_id:
            book_instance = BookAppointmentModel.objects.get(id=book_id)
            book_instance.delete()
            return Response({"message": "successfully removed book request"}, status=HTTP_200_OK)

        return Response({"message": "Incomplete delete book request"}, status=HTTP_400_BAD_REQUEST)
