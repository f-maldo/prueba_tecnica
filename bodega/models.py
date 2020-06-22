from django.db import models


# Create your models here.
class Producto(models.Model):
    id_producto = models.AutoField(primary_key=True)
    nombre_producto = models.CharField(max_length=45)
    estado_producto = models.CharField(
        max_length=1,
        choices=[
            ('0', 'Eliminado'),
            ('1', 'Disponible'),
            ('2', 'En revision')
        ],
        default='1'
    )
    detalle_producto = models.CharField(max_length=45, default='')

    class Meta:
        verbose_name_plural = 'productos'

    def __str__(self):
        return self.nombre_producto


class Bodega(models.Model):
    id_bodega = models.AutoField(primary_key=True)
    nombre_bodega = models.CharField(max_length=45)
    direccion_bodega = models.CharField(max_length=45)
    estado_bodega = models.CharField(
        max_length=1,
        choices=[
            ('0', 'Cerrado'),
            ('1', 'Abierto'),
            ('2', 'En revision')
        ],
        default='1'
    )

    class Meta:
        verbose_name_plural = 'bodegas'

    def __str__(self):
        return self.nombre_bodega


class Orden(models.Model):
    id_bodega = models.ForeignKey('Bodega', on_delete=models.CASCADE)
    id_producto = models.ForeignKey('Producto', on_delete=models.CASCADE)
    cantidad_orden = models.IntegerField()
    fecha_orden = models.DateTimeField()

    class Meta:
        verbose_name_plural = 'ordenes'
