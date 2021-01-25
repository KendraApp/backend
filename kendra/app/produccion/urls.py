from django.urls import path, re_path

from . import views

app_name = 'produccion_app'

urlpatterns = [
    path(
        'api/produccion/',
        views.ListProduccion.as_view(),
        name='produccionlist'
    ),
    path(
        'api/produccion/sabores/',
        views.DetalleSaborProduccion.as_view(),
        name='saborproduccion'
    ),
    path(
        'api/sabores/list/',
        views.SaboresProduccion.as_view(),
        name='sabores'
    ),
    path(
        'api/produccion/create/',
        views.ProduccionCreate.as_view(),
        name='add_resumen_produc'
    ),
    path(
        'api/produccion/add/',
        views.DetalleProduccion.as_view(),
        name='add_datos_produc'
    ),
    path(
        'api/produccion/update/<pk>/',
        views.UpdateGramosProduccion.as_view(),
        name='update_produccion'
    ),
    path(
        'api/produccion/buscar/<pk>/',
        views.ProduccionBuscar.as_view(),
        name='buscar_produccion'
    ),
    path(
        'api/produccion/bases/',
        views.BasesProduccionList.as_view(),
        name='bases_produccion'
    ),
    path(
        'api/produccion/bases/detalle/',
        views.DetalleBaseList.as_view(),
        name='detalle_base'
    ),
    path(
        'api/produccion/consumo/add/',
        views.ConsumoProduccionCreate.as_view(),
        name='consumo_produccion'
    )
]
