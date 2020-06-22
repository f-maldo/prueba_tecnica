from django.contrib import admin
from bodega.models import Producto, Bodega, Orden

# Register your models here.
admin.site.register(Producto)
admin.site.register(Bodega)
admin.site.register(Orden)
