import datetime

from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny



class TodayDateView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        now = datetime.datetime.now()
        date = {
            "date": now.date(),
            "name": now.strftime("%A")
        }
        return Response(date, status=HTTP_200_OK)
