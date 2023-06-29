from django.db import models 

#triagram

class DepartmentManager(models.Manager):
    #managers para modelo autor
    def listar_departamentos(self):
        resultado = self.filter(
            anulate=False
        )
        return resultado