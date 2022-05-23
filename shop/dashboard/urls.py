from django.urls import path
from .category import views as ctg_view
from .product import views as product_view
from views import *

urlpatterns = [
    path('', home, name=home),
    path('ctg/list/', ctg_view.get_ctg, name='dashboard_ctg_list'),
    path('ctg/detail/<int:pk>/', ctg_view.get_one, name='dashboard_ctg_detail')
]