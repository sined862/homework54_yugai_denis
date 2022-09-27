from django.urls import path
from market.views.base import index_view
from market.views.products import detail_view, add_product_view
from market.views.categories import add_category_view


urlpatterns = [
    path('', index_view, name='index'),
    path('product/<int:pk>', detail_view, name='product_detail'),
    path('categories/add', add_category_view, name='add_category'),
    path('products/add', add_product_view, name='add_product'),
    path('products/', index_view, name='products')
]
