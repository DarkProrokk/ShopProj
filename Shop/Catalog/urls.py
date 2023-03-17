from django.urls import path
from .views import index, AllProductView, DetailProductView
urlpatterns = [
    path('', index),
    path('catalog_list/', AllProductView.as_view()),
    path('detail/<int:pk>', DetailProductView.as_view(), name='detail')
]
