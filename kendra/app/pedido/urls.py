from django.urls import path, re_path

from . import views

app_name = 'pedido_app'

urlpatterns = [
    path(
        'api/pedido/',
        views.PedidosList.as_view(),
        name='pedidolist'
    ),
    path(
        'api/pedido/crear/',
        views.CreatePedido.as_view(),
        name='pedidocrear'
    ),

    path(
        'api/pedido/detalle/crear/',
        views.CreateDetalle.as_view(),
        name='pedidodetallecrear'
    ),
    path(
        'api/pedido/detalle/<pedido>/',
        views.DetallePedidoList.as_view(),
        name='pedidodetalle'
    ),
    path(
        'api/pedido/update/<pk>/',
        views.UpdatePedido.as_view(),
        name='pedidodetalle'
    )

]
