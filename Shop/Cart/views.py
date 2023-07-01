from django.shortcuts import render
from .models import Cart
# Create your views here.


def detail_cart(request):
	user = request.user.slug
	cart = Cart.objects.get(user_name=user)
	return render(request, 'Cart/cart_page.html', {'cart':cart})