from django.contrib import admin

from .models import Product, Category, Mark
# Register your models here.
admin.site.register(Category)
admin.site.register(Mark)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
	list_display = ['name', 'price', 'count', 'mark']
	filter_horizontal = ['category']
	list_editable = ['price', 'count', 'mark']
