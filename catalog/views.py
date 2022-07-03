from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse

from catalog.models import Libro
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView

########################################################### LIST VIEW #######################################################################
class List_libros(ListView):
    model = Libro
    template_name = 'catalog/libros.html'
    #queryset = Libro.objects.filter(is_active = True)

########################################################### DETAIL VIEW ######################################################################
class Detail_libro(DetailView):
    model = Libro
    template_name = 'catalog/detalle_libro-html'

########################################################### CREATE VIEW ######################################################################
class Cargar_libro(LoginRequiredMixin, CreateView):
    model = Libro
    template_name = 'catalog/cargar_libro.html'
    fields = '__all__'

    def get_success_url(self):
        return reverse('catalog/detalle_libro', kwargs={'pk':self.object.pk})

########################################################### DELETE VIEW ######################################################################
class Delete_libro(LoginRequiredMixin,DeleteView):
    model = Libro
    template_name = 'catalog/borrar_libro.html'

    def get_success_url (self):
        return reverse('Detail_libro', kwargs ={'pk':self.object.pk})

########################################################### UPDATE VIEW ######################################################################
class Update_libro(LoginRequiredMixin,UpdateView):
    model = Libro
    template_name = 'catalog/update_libro.html'
    fields = '__all__'

########################################################### SEARCH VIEW ######################################################################
def buscar_libro(request):
    libros = Libro.objects.filter(title__icontains=request.GET['search'])
    if libros.exists():
        context = {'libro': libros}
    else:
        context = {'errors':'No se encontro el Libro'}
    return render(request, 'buscar_libro.html', context = context)
