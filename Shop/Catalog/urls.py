from django.urls import path
from .views import index, AllProductView, DetailProductView, AllCategoryView
urlpatterns = [
    path('', index, name='main_page'),
    path('catalog_list/', AllProductView.as_view(), name='catalog'),
    path('detail/<int:pk>', DetailProductView.as_view(), name='detail'),
    path('category_list/', AllCategoryView.as_view(), name='category')
]
