from django.urls import path
from .category import views as ctg_view
from .product import views as product_view
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('ctg/list/', ctg_view.ctg_list, name='dashboard_ctg_list'),
    path('ctg/list/<int:page>', ctg_view.ctg_list, name='dashboard_ctg_list_page'),
    path('ctg/detail/<int:pk>/', ctg_view.ctg_one, name='dashboard_ctg_detail'),
    path('ctg/add/', ctg_view.add_edit, name='dashboard_ctg_add'),
    path('ctg/delete/<int:delete>/', ctg_view.ctg_one, name='dashboard_ctg_delete'),
    path('ctg/edit/<int:pk>/', ctg_view.add_edit, name='dashboard_ctg_edit'),


    path('product/list/', product_view.product_list, name='dashboard_product_list'),
    path('product/list/<int:page>/', product_view.product_list, name='dashboard_product_list_page'),
    path('product/detail/<int:pk>/', product_view.product_one, name='dashboard_product_detail'),
    path('product/delete/<int:delete>/', product_view.product_one, name='dashboard_product_delete'),
    path('product/edit/<int:pk>/', product_view.add_edit, name='dashboard_product_edit'),
    path('product/add/', product_view.add_edit, name='dashboard_product_add'),
]