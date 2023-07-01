from django.urls import path
from .views import *

urlpatterns = [
	path('', detail_cart,name='cart')
]
