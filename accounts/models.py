from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
	phone_number = PhoneNumberField(blank=True)
	full_name = models.CharField(max_length=100)
	is_active = models.BooleanField(default=True)
	is_admin = models.BooleanField(default=False)

	objects = UserManager()

	USERNAME_FIELD = 'phone_number'
	REQUIRED_FIELDS = ['full_name']

	def __str__(self):
		return self.full_name

	@property
	def is_staff(self):
		return self.is_admin


class OtpCode(models.Model):
	phone_number = PhoneNumberField(blank=True)
	code = models.PositiveSmallIntegerField()
	created = models.DateTimeField(auto_now=True)

	def __str__(self):
		return f'{self.phone_number} - {self.code} - {self.created}'