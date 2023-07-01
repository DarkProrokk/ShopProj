from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.
from Catalog.models import Product

class Cart(models.Model):
	user_name = models.CharField(max_length=20, blank=True)
	total_price = models.IntegerField(null=True, blank=True)
	def __str__(self):
		return f'Корзина пользователя - {self.user_name}'

	def save(self, *args, **kwargs):
		total = 0
		for i in self.order_set.all():
			total += i.product_price * i.product_count
		self.total_price = total
		super(Cart, self).save(*args, **kwargs)

class Order(models.Model):
	product_name = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
	product_count = models.IntegerField(blank=True, default=1)
	product_price = models.FloatField(default=0, blank=True, null=True)
	cart_name = models.CharField(max_length=20, null=True)
	cart_info = models.ForeignKey(Cart, on_delete=models.CASCADE)

	def save(self, *args, **kwargs):
		self.cart_name = self.cart_info.user_name
		super(Order, self).save(*args, **kwargs)


	def __str__(self):
		return f'Заказ №{self.pk} c {self.product_name.name} по цене {self.product_price * self.product_count} из корзины пользователя - {self.cart_name}'
