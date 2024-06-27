from django.shortcuts import render, redirect
from .form import PropiedadForm
from .models import Propiedad
from .filters import PropiedadFilter
from django.contrib import messages

# Create your views here.


# Manejador de error cuando la pagina no existe
def error_404_view(request, exception):
    return render(request, "404.html")


# Manejador de error cuando existe internal error
def error_500_view(request):
    return render(request, "500.html")


def lista_propiedades(request):
    objFilter = PropiedadFilter(request.GET, queryset=Propiedad.objects.all())
    context = {"obj": objFilter.qs, "objFilter": objFilter}
    template_name = "lista_propiedades.html"
    return render(request, template_name, context)


def crear_propiedad(request):
    form = PropiedadForm()
    if request.method == "POST":
        form = PropiedadForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Se creo exitosamente la propiedad")
            return redirect("lista_propiedades")
    template_name = "propiedad_form.html"
    context = {"form": form}
    return render(request, template_name, context)


def actualizar_propiedad(request, id):
    propiedad = Propiedad.objects.get(id=id)
    form = PropiedadForm(instance=propiedad)
    if request.method == "POST":
        form = PropiedadForm(request.POST, instance=propiedad)
        if form.is_valid():
            form.save()
            messages.success(request, "Se actualizó la propiedad")
            return redirect("lista_propiedades")
    template_name = "propiedad_form.html"
    context = {"form": form, "obj": propiedad}
    return render(request, template_name, context)


def borrar_propiedad(request, id):
    obj = Propiedad.objects.get(id=id)
    if request.method == "POST":
        obj.delete()
        messages.success(request, "Se borró la propiedad")
        return redirect("lista_propiedades")
    template_name = "confirmation.html"
    context = {"obj": obj}
    return render(request, template_name, context)
