from django import forms 

from .models import Empleado

#Modelo + Fromulario
class EmpleadoForm(forms.ModelForm):
    
    class Meta:

        model = Empleado
        fields = (''
            'first_name',
            'last_name',
            'gender',
            'department',
            'image',
            'skills',
        )
        widgets ={
            'skills':forms.CheckboxSelectMultiple()
        }




