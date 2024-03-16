from rest_framework.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from django.db.models import Q

from ..serializers.register import UserRegistrationSerializer
from user.models import UserAccount


class UserRegistrationView(APIView):
    """Users can register their account by email, frist_name, last_name and password."""

    permission_classes = [AllowAny]

    def validate_parameter(self, phone_number, email, password):
        if phone_number and email and password:
            return True
        else:
            return False

    def have_account(self, phone_number, email):
        #    check this phone_number exists or email using complex query with OR operation.
        is_member = UserAccount.objects.filter(
            Q(phone_number=phone_number) | Q(email=email)
        ).exists()
        return is_member

    def post(self, request, *args, **kwargs):
        phone_number = request.data.get("phone_number")
        email = request.data.get("email")
        password = request.data.get("password")

        if self.validate_parameter(phone_number, email, password) is True:
            if self.have_account(phone_number, email) is True:
                return Response({"message":"You have already account at DocMeet"}, status=HTTP_400_BAD_REQUEST)
            user_data = {
                "phone_number": phone_number,
                "email": email,
                "password": password,
                "user_type":"DOCTOR",
                "is_doctor":True,
            }

            serializer = UserRegistrationSerializer(data=user_data)
            if serializer.is_valid():
                serializer.save()

                return Response({"message":"Completed your registration process!"}, status=HTTP_201_CREATED)

        return Response({"message":"Incompleted registration! Please provide valid data"}, status=HTTP_400_BAD_REQUEST)
