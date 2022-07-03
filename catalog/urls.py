from django.urls import path
from catalog.views import Cargar_libro, Detail_libro, Update_libro, List_libros,Delete_libro,buscar_libro


app_name = 'catalog'

urlpatterns = [
    path('cargar-libro/', Cargar_libro.as_view(), name = 'cargar_libro'),
    path('detail-libro/<int:pk>/', Detail_libro.as_view(), name ='detail_libro'),
    path('update-libro/<int:pk>/', Update_libro.as_view(), name ='update_libro'),
    path('list-libros/', List_libros.as_view(), name ='list_libros'),
    path('delete-libro/<int:pk>/', Delete_libro.as_view(), name ='delete_libro'),
    path('buscar-libro/', buscar_libro, name = 'buscar_libro')
]












