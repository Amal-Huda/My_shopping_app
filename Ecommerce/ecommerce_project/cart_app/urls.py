from django.urls import path
from .import views
app_name='cart_app'

urlpatterns=[
    path('',views.cart_detail,name='cart_detail'),
    path('add/<product_id>/',views.add_to_cart,name='add_to_cart'),
    path('remove/<int:product_id>/',views.remove_from_cart,name='cart_remove'),
    path('full_remove/<int:product_id>/',views.remove_full,name='full_remove')
]