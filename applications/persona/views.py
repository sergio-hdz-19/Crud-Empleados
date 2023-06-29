from django.shortcuts import render
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import(  
ListView,
DetailView,
CreateView,
TemplateView,
UpdateView,
DeleteView
)

#models
from .models import Empleado
#forms
from .forms import EmpleadoForm
from django.contrib.messages.views import SuccessMessageMixin

class InicioView(TemplateView):
    #Vista que carga pagina de Inicio
    template_name = 'inicio.html'




# 1 Lista todos los empleados de la empresa
class ListAllEmpleados(ListView):
    template_name = 'persona/list_all.html'
    paginate_by = 4
    ordering = 'first_name'
    context_object_name = 'empleados'
    
    
    def get_queryset(self):
        palabra_clave = self.request.GET.get("kword", '')
        return Empleado.objects.listar_empleados(palabra_clave)

    



class ListAllEmpleadosAdmin(ListView):
    template_name = 'persona/lista_empleados.html'
    paginate_by = 10
    ordering = 'first_name'
    context_object_name = 'empleados'
    model = Empleado
    


# 2 Lista todos los empleados que pertenecen a un area de la empresa 

class ListByAreaEmpleado(ListView):
    template_name = 'persona/list_by_area.html'
    context_object_name = 'empleados'

    def get_queryset(self):
        area = self.kwargs['shorname']
        lista = Empleado.objects.filter(
            department__shor_name = area,
            anulate=False
        )
        return lista 


# 3 Listar empleados por trabjo
class ListByJob(ListView):
    template_name = 'persona/list_by_job.html'
    

    def get_queryset(self):
        trabajo = self.kwargs['gender']
        lista = Empleado.objects.filter(
            gender = trabajo
        )
        return lista 





# 4 Listar empleados palabra clave


class ListEmpleadoByKword(ListView):
    template_name = 'persona/by_kword.html'
    context_object_name = 'empleados'

    def get_queryset(self):
        palabra_clave = self.request.GET.get("kword",'')
        lista = Empleado.objects.filter(
            first_name = palabra_clave
        )
        return lista


# 5 listar habilidades de un empleado

class ListHabilidades(ListView):
    template_name = 'persona/habilidades.html'
    context_object_name = 'habilidades'

    def get_queryset(self):
        palabra_clave = self.request.GET.get("kword")
        if(palabra_clave != None):
            empleado = Empleado.objects.get(id=palabra_clave)
            lista = empleado.skills.all()
        else:
            lista = []
        return lista 


class EmpleadoDetailView(DetailView):
    model = Empleado
    template_name = "persona/detail_empleado.html"

    def get_context_data(self, **kwargs):
        context = super(EmpleadoDetailView,self).get_context_data(**kwargs)
        context['titulo'] = 'Empleado del mes'
        return context
    


class SuccessView(TemplateView):
    template_name = "persona/success.html"


class EmpleadoCreateView(SuccessMessageMixin,CreateView):
    model = Empleado
    template_name = "persona/add.html"
    form_class = EmpleadoForm
    success_url = reverse_lazy('persona_app:empleado_add')
    success_message = " %(first_name)s se agrego correctamente"
    
    
    def form_valid(self, form):
        empleado = form.save(commit=False)
        empleado.full_name = empleado.first_name + ' ' + empleado.last_name
        empleado.save()
        return super(EmpleadoCreateView,self).form_valid(form)

    def get_success_message(self, cleaned_data):
        return self.success_message % cleaned_data



class EmpleadoUpdateView(UpdateView):
    model = Empleado
    template_name = "persona/update.html"
    form_class = EmpleadoForm
    success_url = reverse_lazy('persona_app:empleado_admin')

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        return super(EmpleadoUpdateView,self).form_valid(form)


class EmpleadoDeleteView(SuccessMessageMixin,DeleteView):
    model = Empleado
    template_name = "persona/delete.html"
    success_url = reverse_lazy('persona_app:empleado_admin')
    
