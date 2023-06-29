from django.db import models 

#triagram

class EmpleadoManager(models.Manager):
    #managers para modelo autor
    def listar_empleados(self,kword):
        resultado = self.filter(
            first_name__icontains=kword,
            anulate=False,
            department__anulate=False
            
        
        ).order_by('first_name')
        return resultado