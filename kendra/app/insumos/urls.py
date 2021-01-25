from django.urls import path, re_path

from . import views

app_name = 'insumos_app'

urlpatterns = [
    path(
        'api/insumos/',
        views.ListInsumos.as_view(),
        name='insumoslist'
    ),
    path(
        'api/insumos/update/<pk>/',
        views.UpdateGramosInsumos.as_view(),
        name='update_insumos'
    ),
    path(
        'api/insumos/buscar/<pk>/',
        views.InsumosBuscar.as_view(),
        name='buscar_insumos'
    ),
    path(
        'api/shopinsumos/',
        views.CompraInsumos.as_view(),
        name='add_comprainsumos'
    ),
    path(
        'api/shopinsumos/add/',
        views.AddCompraInsumos.as_view(),
        name='add_comprainsumos'
    ),
    path(
        'api/insumos/unidadmedida/',
        views.ListUnidadMedida.as_view(),
        name='list_unidadmedida'
    ),
    path(
        'api/insumos/consumo/',
        views.ConsumoList.as_view(),
        name='list_consumo',
    ),
    path(
        'api/insumos/consumo/add/',
        views.ConsumoCreate.as_view(),
        name='create_consumo',
    )
]
