from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('ingreso/<int:opcion_ingreso>/', views.ingreso, name='ingreso'),
    path('edicion/<int:opcion_edicion>/', views.edicion, name='edicion'),
    path('edicion/item/<int:tipo>/<int:pk>/', views.edicion_item, name='edicion_item'),
    path('eliminar/item/<int:tipo>/<int:pk>/', views.eliminar_item, name='eliminar_item'),
]
