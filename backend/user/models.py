from django.conf import settings
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)
from django.db import models

from specialization.models import SpecializationModel
from religion.models import ReligionModel
from utils.utils import PHONE_REGEX
from utils.models import CommonInfo


class UserAccountManager(BaseUserManager):
    def create_user(self, phone_number, password=None):
        if not phone_number:
            raise ValueError("Phone Number is required !")
        if not password:
            raise ValueError("Password is must !")

        user = self.model(
            phone_number=phone_number,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, phone_number, password):
        user = self.create_user(
            phone_number=phone_number,
            password=password,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class UserAccount(AbstractBaseUser, PermissionsMixin, CommonInfo):
    phone_number = models.CharField(
        validators=[PHONE_REGEX], max_length=11, unique=True
    )
    email = models.EmailField(max_length=255, unique=True, null=True, blank=True)
    class UserType(models.TextChoices):
        PATIENT = "PATIENT", "patient"
        DOCTOR = "DOCTOR", "doctor"

    user_type = models.CharField(
        max_length=10, choices=UserType.choices, null=True, blank=True
    )
    first_name = models.CharField(max_length=255, null=True, blank=True)
    last_name = models.CharField(max_length=255, null=True, blank=True)
    emergency_contact = models.CharField(
        validators=[PHONE_REGEX], max_length=11, null=True, blank=True
    )

    class Gender(models.TextChoices):
        MALE = "MALE", "male"
        FEMALE = "FEMALE", "female"
        OTHERS = "OTHERS", "others"

    gender = models.CharField(
        max_length=10, choices=Gender.choices, null=True, blank=True
    )
    date_of_birth = models.DateField(null=True, blank=True)
    blood_group = models.CharField(max_length=255, null=True, blank=True)
    religion = models.CharField(max_length=255, null=True, blank=True)

    class MaritalStatus(models.TextChoices):
        UNMARRIED = "UNMARRIED", "unmarried"
        MARRIED = "MARRIED", "married"
        OTHERS = "OTHERS", "others"

    marital_status = models.CharField(
        max_length=10, choices=MaritalStatus.choices, null=True, blank=True
    )
    nationality = models.CharField(max_length=255, null=True, blank=True)
    occupation = models.CharField(max_length=255, null=True, blank=True)
    qualification = models.CharField(max_length=255, null=True, blank=True)
    specialization = models.ForeignKey(
        SpecializationModel, on_delete=models.DO_NOTHING, null=True, blank=True
    )
    picture = models.URLField(null=True, blank=True)
    is_admin = models.BooleanField(default=False)
    is_patient = models.BooleanField(default=False)
    is_doctor = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = "phone_number"

    objects = UserAccountManager()

    def __str__(self):
        return self.phone_number

    class Meta:
        verbose_name = "UserAccount"
        verbose_name_plural = "UserAccounts"
        db_table = "user_account"


class PatientManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return (
            super()
            .get_queryset(*args, **kwargs)
            .filter(user_type=UserAccount.UserType.PATIENT)
        )


class DoctorManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return (
            super()
            .get_queryset(*args, **kwargs)
            .filter(user_type=UserAccount.UserType.DOCTOR)
        )


class Patient(UserAccount):
    user_type = UserAccount.UserType.PATIENT
    objects = PatientManager()

    class Meta:
        proxy = True

    def save(self, *args, **kwargs):
        if not self.pk:
            self.user_type = UserAccount.UserType.PATIENT
        return super().save(*args, **kwargs)


class Doctor(UserAccount):
    user_type = UserAccount.UserType.DOCTOR
    objects = DoctorManager()

    class Meta:
        proxy = True

    def save(self, *args, **kwargs):
        if not self.pk:
            self.user_type = UserAccount.UserType.DOCTOR
        return super().save(*args, **kwargs)
