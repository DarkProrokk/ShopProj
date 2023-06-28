from django.contrib import admin

from .models import Product, Mark, Category

# Register your models here.
admin.site.register(Category)
admin.site.register(Mark)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
	list_display = ['name', 'price', 'count', 'mark']
	list_editable = ['price', 'count', 'mark']
