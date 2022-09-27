from django.urls import path
from market.views.base import index_view


urlpatterns = [
    path('', index_view, name='index'),
]
