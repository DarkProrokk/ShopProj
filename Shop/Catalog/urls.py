from django.urls import path
from .views import index, AllProductView, DetailProductView, category, child_cat, main_cat
urlpatterns = [
    path('', index, name='main_page'),
    path('catalog_list/', AllProductView.as_view(), name='catalog'),
    path('detail/<int:pk>', DetailProductView.as_view(), name='detail'),
    path('category_list/', category, name='category'),
    path('calalog_list/maincat/<slug:slug_category>', child_cat, name='childcat'),
    path('calalog_list/<slug:slug_category>', main_cat, name='maincat'),
]
