from django.urls import path
from .category.views import CtgView
from .product.views import ProductView

urlpatterns = [
    path('category/', CtgView.as_view(), name='api_ctg_list'),
    path('category/<int:pk>', CtgView.as_view(), name='api_ctg_one'),
    path('product/', ProductView.as_view(), name='api_product_list'),
    path('product/<int:pk>', ProductView.as_view(), name='api_product_one')
]
