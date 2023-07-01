from django.db import models
from django.utils.text import slugify
from pytils.translit import slugify


# Create your models here.


class Category(models.Model):
	name = models.CharField(max_length=30)
	parent = models.ForeignKey(
		'self',
		on_delete=models.PROTECT,
		null=True,
		blank=True,
	)
	slug = models.SlugField(default=' ', null=True, blank=True)

	def save(self, *args, **kwargs):
		self.slug = slugify(self.name)
		super(Category, self).save(*args, **kwargs)

	def __str__(self):
		return f'{self.name} | parent - {self.parent}' if self.parent else self.name


class Mark(models.Model):
	name = models.CharField(max_length=30)

	def __str__(self):
		return f'{self.name}'


class Product(models.Model):
	name = models.CharField(max_length=30)
	price = models.FloatField(default=0)
	count = models.IntegerField(default=0)
	category = models.ForeignKey(Category, on_delete=models.PROTECT, null=True)
	mark = models.ForeignKey(Mark, on_delete=models.PROTECT, null=True)
	description = models.TextField(max_length=200)
	photo = models.ImageField(upload_to=f'img/', blank=True, null=True)

