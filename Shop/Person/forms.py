from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from Person.models import CustomUser




class CustomUserCreationForm(UserCreationForm):
	class Meta:
		model = CustomUser
		fields = ('username', 'fio', 'gender', 'birth_date')