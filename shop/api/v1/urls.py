from django.urls import path
from .category.views import CtgView

urlpatterns = [
    path('category/', CtgView.as_view(), name='api_ctg_list'),
    path('category/<int:pk>', CtgView.as_view(), name='api_ctg_one')
]
