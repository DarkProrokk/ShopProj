from django.shortcuts import get_list_or_404, get_object_or_404
from django.shortcuts import render, redirect
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
	name = Category.objects.filter(slug=slug_category)[0].name
	select = get_list_or_404(Product, category=select_cat)
	print(select)
	return render(request, 'Catalog/selected_category.html', {'selected': [select], 'cat_name':name})

def main_cat(request, slug_category: str):
	select_cat = Category.objects.filter(slug=slug_category)[0]
	all_cat = []
	for i in select_cat.category_set.all():
		prod = Product.objects.filter(category=i)
		all_cat.append(prod)
	return render(request, 'Catalog/selected_category.html', {'selected': all_cat, 'cat_name':select_cat.name})

def add_prod(request):
	if request.method == "POST":
		order_from_page = request.POST.get
		product_count = int(order_from_page('number'))
		product_id = order_from_page('prod')
		prod_obj = Product.objects.get(pk=product_id)
		if 0 < product_count <= prod_obj.count:
			request.user.user_cart.order_set.create(product_name=prod_obj, product_count=product_count, product_price=prod_obj.price)
			prod_obj.count = prod_obj.count - product_count
			prod_obj.save()
	return redirect('catalog')