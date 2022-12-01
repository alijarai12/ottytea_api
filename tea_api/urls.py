from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('product/', include('product.urls')),

    path('auth/', include('registration.urls')),

    path('carts/', include('cart_item.urls')),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
