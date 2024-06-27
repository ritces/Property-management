from django.urls import path
from .views import (
    lista_propiedades,
    crear_propiedad,
    actualizar_propiedad,
    borrar_propiedad,
)

urlpatterns = [
    path("", lista_propiedades, name="lista_propiedades"),
    path("crear/", crear_propiedad, name="crear_propiedad"),
    path("actualizar/<int:id>", actualizar_propiedad, name="actualizar_propiedad"),
    path("borrar/<int:id>", borrar_propiedad, name="borrar_propiedad"),
]

handle404 = "propiedades.views.error_404_view"
handler500 = "propiedades.views.error_500_view"
