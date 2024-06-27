from django import forms
from .models import Propiedad


class PropiedadForm(forms.ModelForm):
    class Meta:
        model = Propiedad
        fields = "__all__"

        labels = {
            "nombre": "Nombre",
            "direccion": "Direccion",
            "codigo_postal": "Codigo Postal",
            "pais": "Pais",
            "ciudad": "Ciudad",
            "superficie": "Superficie",
            "tipos_opciones": "Tipo",
        }

        widgets = {
            "nombre": forms.TextInput(attrs={"required": True}),
            "pais": forms.TextInput(attrs={"required": True}),
            "direccion": forms.TextInput(attrs={"required": True}),
            "codigo_postal": forms.NumberInput(attrs={"required": True}),
            "superficie": forms.NumberInput(attrs={"required": True}),
            "ciudad": forms.TextInput(attrs={"required": True}),
            "tipos_opciones": forms.Select(attrs={"required": True}),
        }
