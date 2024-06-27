import django_filters
from django_filters import RangeFilter

from .models import Propiedad


class PropiedadFilter(django_filters.FilterSet):
    superficie = RangeFilter()

    class Meta:
        model = Propiedad
        fields = "__all__"
        exclude = ["direccion", "codigo_postal", "nombre"]
