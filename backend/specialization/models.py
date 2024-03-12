from django.db import models


class SpecializationModel(models.Model):
    specialized_name = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.specialized_name

    class Meta:
        verbose_name = "Specialization"
        verbose_name_plural = "Specializations"
        db_table = "specialization"
