from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Product


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
