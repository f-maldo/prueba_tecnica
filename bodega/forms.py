from django import forms
from .models import Producto, Bodega


class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = (
            'nombre_producto',
            'estado_producto',
            'detalle_producto'
        )


class BodegaForm(forms.ModelForm):
    class Meta:
        model = Bodega
        fields = (
            'nombre_bodega',
            'direccion_bodega',
            'estado_bodega'
        )