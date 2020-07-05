from django.urls import path

from .views import (
    product_detail_view, 
    product_create_view,
    dynamic_lookup_view,
    product_delete_view,
    product_list_view
)
app_name = "products"
urlpatterns = [
    path('', product_list_view, name='product-list'),
    path('create/', product_create_view, name='product-create'),
    #path('product/', product_detail_view, name='product-detail'),
    path('<int:id>/', dynamic_lookup_view, name='product-detail'),
    path('<int:id>/delete/', product_delete_view, name='product-delete'),
]