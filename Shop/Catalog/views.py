from django.shortcuts import get_list_or_404, get_object_or_404
from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import *
from Cart.models import Cart

# Create your views here.
def index(request):
	return render(request, 'Catalog/index.html')


class AllProductView(ListView):
	template_name = 'Catalog/Catalog.html'
	model = Product
	context_object_name = 'all_prod'

	def get_queryset(self):
		queryset = super().get_queryset()
		return queryset


class DetailProductView(DetailView):
	model = Product
	template_name = 'Catalog/product_info.html'


def category(request):
	cat = Category.objects.filter(parent__isnull = True)
	return render(request, 'Catalog/category.html', {'mainCat':cat})


def child_cat(request, slug_category: str):
	select_cat = get_object_or_404(Category, slug=slug_category)
	select = get_list_or_404(Product, category=select_cat)
	print(select)
	return render(request, 'Catalog/selected_category.html', {'selected': [select]})

def main_cat(request, slug_category: str):
	select_cat = Category.objects.filter(slug=slug_category)[0].category_set.all()
	all_cat = []
	for i in select_cat:
		prod = Product.objects.filter(category=i)
		all_cat.append(prod)
	return render(request, 'Catalog/selected_category.html', {'selected': all_cat})
