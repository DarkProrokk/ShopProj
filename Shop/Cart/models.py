from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
# Create your models here.

class CartData(models.Model):
	product_name = models.CharField(max_length=40, blank=True, null=True)
	product_count = models.IntegerField(blank=True, default=1)
	product_price = models.FloatField(default=0, blank=True, null=True)
	cart_data_name = models.CharField(max_length=20)

	def __str__(self):
		return f'Данные корзины пользователя - {self.cart_data_name}'

class Cart(models.Model):
	user_name = models.CharField(max_length=20, blank=True)
	cart_info = models.OneToOneField(CartData, blank=True, on_delete=models.CASCADE, null=True)

	def save(self, *args, **kwargs):
		super(Cart, self).save()
		self.cart_info = CartData.objects.get(cart_data_name=self.user_name)

	def __str__(self):
		return f'Корзина пользователя - {self.user_name}'

@receiver(pre_save, sender=Cart)
def create_cartdata(sender, instance, **kwargs):
	cart_user = instance.user_name
	if not CartData.objects.filter(cart_data_name=cart_user):
		CartData.objects.create(cart_data_name=cart_user)