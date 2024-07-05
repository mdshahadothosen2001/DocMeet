from django.db import models

from user.models import Doctor
from utils.models import TimeStamp

class AppointmentModel(TimeStamp):
    doctor = models.ForeignKey(
        Doctor, on_delete=models.DO_NOTHING
    )
    day = models.CharField(max_length=100, null=True, blank=True)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    availability = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.day} {self.doctor}"

    class Meta:
        verbose_name = "Appointment"
        verbose_name_plural = "Appointments"
        db_table = "appointment"
