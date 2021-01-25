from django.contrib import admin
from django.urls import path, re_path, include
from django.conf import settings
from django.conf.urls.static import static


admin.site.site_header = 'Panel de administración: Kendra App'

urlpatterns = [
    path('ruadmin/', admin.site.urls),
    re_path('', include('app.preparacion.urls')),
    re_path('', include('app.produccion.urls')),
    re_path('', include('app.insumos.urls')),
    re_path('', include('app.pedido.urls')),
    re_path('', include('app.facturas.urls'))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
