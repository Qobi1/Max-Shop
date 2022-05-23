from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('error/', error, name='error'),
    path('about/', about, name='about'),
    path('blog-post/', blog_post, name='blog_post'),
    path('blog/', blog, name='blog'),
    path('cart/', cart, name='cart'),
    path('checkout/', checkout, name='checkout'),
    path('contact/', contact, name='contact'),
    path('index2/', index2, name='index2'),
    path('shop/', shop, name='shop'),
    path('shop_single/', shop_single, name='shop_single'),
]