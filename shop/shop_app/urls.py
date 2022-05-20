from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('error/', error, name='index'),
    path('about/', about, name='index'),
    path('blog-post/', blog_post, name='index'),
    path('blog/', blog, name='index'),
    path('cart/', cart, name='index'),
    path('checkout/', checkout, name='index'),
    path('contact/', contact, name='index'),
    path('index2/', index2, name='index'),
    path('shop/', shop, name='index'),
    path('shop-single', shop_single, name='index'),
]