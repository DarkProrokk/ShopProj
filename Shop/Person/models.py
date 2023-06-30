from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from pytils.translit import slugify

from Cart.models import Cart


# Create your models here.
class CustomUser(AbstractUser):
	GENDERS = {
		('M', 'Мужчина'),
		('F', 'Женщина')
	}
	slug = models.SlugField(default=' ', null=True, blank=True)
	fio = models.CharField(max_length=20, default='')
	gender = models.CharField(max_length=20, choices=GENDERS, default='')
	birth_date = models.DateField(default='2000-01-01')
	user_cart = models.OneToOneField(Cart, on_delete=models.CASCADE, null=True)

	def save(self, *args, **kwargs):
		self.slug = slugify(self.username)
		super(CustomUser, self).save(*args, **kwargs)
		self.user_cart = Cart.objects.get(user_name=self.slug)
		super(CustomUser, self).save(*args, **kwargs)

@receiver(pre_save, sender=CustomUser)
def create_cart(sender, instance, **kwargs):
	cart_user = instance.slug
	if not Cart.objects.filter(user_name=cart_user):
		Cart.objects.create(user_name=cart_user)