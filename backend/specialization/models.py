from django.db import models


class SpecializationModel(models.Model):
    specialized_name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    picture = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.specialized_name

    class Meta:
        verbose_name = "Specialization"
        verbose_name_plural = "Specializations"
        db_table = "specialization"
