from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from book_appointment.models import BookAppointmentModel
from utils.custom_permission import IsDoctor
from utils.utils import tokenValidation
from ..serializers.book_list import BookAppointmentListSerializer


class BookAppointmentListView(APIView):
    permission_classes = [IsDoctor]

    def get(self, request):
        doctor =  tokenValidation(request)["id"]
        books =BookAppointmentModel.objects.filter(appointment__doctor=doctor, is_complete=True, is_active=True)
        serializer = BookAppointmentListSerializer(books, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
