from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from .forms import ProductoForm, BodegaForm
from .models import Producto, Bodega
# from django.http import HttpResponse
# return HttpResponse("Prueba de la opcion %s" % opcion_ingreso)


# Create your views here.
def index(request):
    return render(request, 'bodega/index.html')


def ingreso(request, opcion_ingreso):
    if opcion_ingreso == 1:
        if request.method == 'POST':
            form = ProductoForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('index')
        else:
            form = ProductoForm()
        return render(request, 'bodega/ingreso.html', {'form': form, 'name': 'Producto'})

    elif opcion_ingreso == 2:
        if request.method == 'POST':
            form = BodegaForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('index')
        else:
            form = BodegaForm()
        return render(request, 'bodega/ingreso.html', {'form': form, 'name': 'Bodega'})


def edicion(request, opcion_edicion):
    if opcion_edicion == 1:
        lista = Producto.objects.exclude(estado_producto=0)
        return render(request, 'bodega/listado_editar.html', {'lista': lista, 'name': 'Producto', 'tipo': 1})
    elif opcion_edicion == 2:
        lista = Bodega.objects.exclude(estado_bodega=0)
        return render(request, 'bodega/listado_editar.html', {'lista': lista, 'name': 'Bodega', 'tipo': 2})


def edicion_item(request, pk, tipo):
    if tipo == 1:
        item = get_object_or_404(Producto, pk=pk)
        if request.method == "POST":
            form = ProductoForm(request.POST, instance=item)
            if form.is_valid():
                item = form.save(commit=False)
                item.save()
                return redirect('index')
        else:
            form = ProductoForm(instance=item)
        return render(request, 'bodega/ingreso.html', {'form': form})
    elif tipo == 2:
        item = get_object_or_404(Bodega, pk=pk)
        if request.method == "POST":
            form = BodegaForm(request.POST, instance=item)
            if form.is_valid():
                item = form.save(commit=False)
                item.save()
                return redirect('index')
        else:
            form = BodegaForm(instance=item)
        return render(request, 'bodega/ingreso.html', {'form': form})


def eliminar_item(request, pk, tipo):
    if tipo == 1:
        item = get_object_or_404(Producto, pk=pk)
        item.estado_producto = 0
        item.save()
        return redirect('index')
    elif tipo == 2:
        item = get_object_or_404(Bodega, pk=pk)
        item.estado_bodega = 0
        item.save()
        return redirect('index')


def actualizar_stock(request):
    pass
