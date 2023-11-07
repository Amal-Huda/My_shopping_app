from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from . import views
app_name='ecommerce_app'
urlpatterns = [
    path('',views.allProdCat,name='allProdCat'),
    path('<slug:c_slug>/',views.allProdCat,name='Products_by_category'),
    path('<slug:c_slug>/<slug:p_slug>/',views.ProductDetails,name='Product_details'),
    # path('',include('ecommerce_app.urls')),
]
if settings.DEBUG:
    urlpatterns+=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)