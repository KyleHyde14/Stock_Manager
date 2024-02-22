from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create_store', views.create_store, name='create_store'), 
    path('stock/<int:store_id>', views.stores_stock, name='stores_stock'),
    path('create_product', views.create_product, name='create_product'),
    path('products/<int:user_id>', views.products, name='products'),
    path('add_product/<int:store_id>', views.add_product, name='add_product'),
    path('modify_cart', views.modify_cart, name='modify_cart')
]