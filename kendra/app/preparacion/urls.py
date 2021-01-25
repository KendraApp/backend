from django.urls import path, re_path

from . import views

app_name = 'productos_app'

urlpatterns = [
    path(
        'api/productos/',
        views.ListProductos.as_view(),
        name='productoslist'
    ),
    path(
        'api/productos/adicion/',
        views.ListProductosAdicion.as_view(),
        name='productoslist'
    ),
    path(
        'api/productos/insumos/',
        views.InsumosProductosList.as_view(),
        name='insumosproducto'
    ),
    path(
        'api/productos/<producto>/',
        views.DetalleProductos.as_view(),
        name='detalleproducto'
    ),

]
