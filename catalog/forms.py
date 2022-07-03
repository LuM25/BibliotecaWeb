from turtle import width
from django import forms
from catalog.models import Libro

class FormCargarLibro (forms.Libro):
    class Meta:
        model = Libro
        fields = '__all__'
        