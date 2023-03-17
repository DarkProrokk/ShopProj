from django.db import models


# Create your models here.
class Category(models.Model):
	name = models.CharField(max_length=30)

	def __str__(self):
		return f'{self.name}'


class Mark(models.Model):
	name = models.CharField(max_length=30)

	def __str__(self):
		return f'{self.name}'


class Product(models.Model):
	name = models.CharField(max_length=30)
	price = models.FloatField(default=0)
	count = models.IntegerField(default=0)
	category = models.ManyToManyField(Category, related_name='product')
	mark = models.ForeignKey(Mark, on_delete=models.PROTECT, null=True)
	description = models.TextField(max_length=200)
