from rest_framework.permissions import BasePermission

from utils.utils import tokenValidation


class IsPatient(BasePermission):
    def has_permission(self, request, view):
        payload = tokenValidation(request)
        if payload["is_doctor"] is False:
            return True
        else:
            False


class IsDoctor(BasePermission):
    def has_permission(self, request, view):
        payload = tokenValidation(request)
        if payload["is_doctor"] is True:
            return True
        else:
            False