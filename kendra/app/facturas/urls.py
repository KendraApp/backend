from django.urls import path, re_path

from . import views

app_name = 'facturas_app'

urlpatterns = [
    path(
        'api/facturas/',
        views.FacturaList.as_view(),
        name='facturalist'
    ),
    path(
        'api/facturas/add/',
        views.FacturasAdd.as_view(),
        name='pedidoadd'
    ),
]
