from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class CustomUser(AbstractUser):
	GENDERS = {
		('M', 'Мужчина'),
		('F', 'Женщина')
	}
	fio = models.CharField(max_length=20, default='')
	gender = models.CharField(max_length=20,choices=GENDERS, default='')
	birth_date = models.DateField(default='2000-01-01')
# password = models.
