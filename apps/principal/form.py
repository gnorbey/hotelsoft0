from django import forms
from apps.principal.models import Habitacion


class HabitacionForm(forms.ModelForm):

    class Meta:
        model = Habitacion
        


        fields= [
            
            
            'numero',
            'estado',
            'costo',
            'descripcion',
            'tipo',

        ]
        labels= {
            
            'numero': 'Numero',
            'estado': 'Estado',
            'costo': 'Costo',
            'descripcion': 'Descripcion',
            'tipo': 'Tipo',
        }
        widgets = {
            
            'numero': forms.TextInput(attrs={'class': 'form-control'}),
            'estado': forms.Select(attrs={'class': 'form-control'}),
            'costo': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.TextInput(attrs={'class': 'form-control'}),
            'tipo':forms.Select(attrs={'class': 'form-control'}),
        } 
# class SolicitudForm(forms.ModelForm):
#     class Meta:
#         model=Solicitud
#         fields = [
#             '',
#             '',]
        