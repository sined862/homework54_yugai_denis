from django.urls import path
from market.views.base import index_view
from market.views.products import detail_view


urlpatterns = [
    path('', index_view, name='index'),
    path('product/<int:pk>', detail_view, name='product_detail')
]
