from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from book_appointment.models import BookAppointmentModel
from utils.custom_permission import IsDoctor
from ..serializers.book_list import BookAppointmentListSerializer


class BookAppointmentListView(APIView):
    permission_classes = [IsDoctor]

    def get(self, request):
        books =BookAppointmentModel.objects.all()
        serializer = BookAppointmentListSerializer(books, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
