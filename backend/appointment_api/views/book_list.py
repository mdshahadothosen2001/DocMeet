from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny

from book_appointment.models import BookAppointmentModel
from utils.custom_permission import IsDoctor
from ..serializers.book_list import BookAppointmentListSerializer


class BookAppointmentListView(APIView):
    permission_classes = [IsDoctor]

    def get(self, request):
        books =BookAppointmentModel.objects.all()
        serializer = BookAppointmentListSerializer(books, many=True)
        return Response(serializer.data, status=HTTP_200_OK)
