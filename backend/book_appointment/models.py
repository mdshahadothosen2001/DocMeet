from django.db import models

from utils.models import CommonInfo
from user.models import Patient
from appointment.models import AppointmentModel


class BookAppointmentModel(CommonInfo):
    patient = models.ForeignKey(Patient, on_delete=models.DO_NOTHING)
    appointment = models.ForeignKey(AppointmentModel, on_delete=models.DO_NOTHING)
    is_complete = models.BooleanField(default=False)

    def __str__(self):
        return str(self.is_complete)

    class Meta:
        verbose_name = "Book Appointment"
        verbose_name_plural = "Book Appointments"
        db_table = "book_appointment"
