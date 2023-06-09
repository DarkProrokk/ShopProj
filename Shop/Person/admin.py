from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
	model = CustomUser

	add_fieldsets = (
		*UserAdmin.add_fieldsets,
		(
			'Custom fields',
			{
				'fields': (
					'fio',
					'gender',
					'birth_date',
					'slug',
					'user_cart',
				)
			}
		)
	)
	fieldsets = (
		*UserAdmin.fieldsets,
		(
			'Custom fields',
			{
				'fields': (
					'fio',
					'gender',
					'birth_date',
					'slug',
					'user_cart'
				)
			}
		)
	)