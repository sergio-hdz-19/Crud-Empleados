from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import FormView

from .forms import NewDepartamentoForm
from applications.persona.models import Empleado
from .models import Department


class DepartamentoListView(ListView):
    model = Department
    template_name='departamento/lista.html'
    context_object_name = 'departamentos'
    
    def get_queryset(self):
        return Department.objects.listar_departamentos()


class NewDepartamentoView(FormView):
    template_name = 'departamento/new_departamento.html'
    form_class = NewDepartamentoForm
    success_url = '/' 

    def form_valid(self,form):
        print("estamos en el form valiud")

        depa = Department(
            name=form.cleaned_data['departamento'],
            shor_name=form.cleaned_data['shorname']
        )
        depa.save()

        nombre = form.cleaned_data['nombre']
        apellido = form.cleaned_data['apellidos']
        Empleado.objects.create(
            first_name = nombre,
            last_name = apellido,
            gender = '3',
            department = depa
        )
        return super(NewDepartamentoView,self).form_valid(form)
















