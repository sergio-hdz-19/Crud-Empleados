from django.db import models
from .managers import DepartmentManager
# Create your models here.

class Department(models.Model):
    name = models.CharField('Nombre',max_length=50, blank=True, null=True)
    shor_name = models.CharField('Nombre Corto',max_length=20, unique=True)
    anulate = models.BooleanField('Anulado',default=False)
    objects = DepartmentManager()

    class Meta:
        verbose_name = 'Department'
        verbose_name_plural = 'Departments'
        ordering = ['id']
        unique_together = ('name','shor_name')

        
    def __str__(self):
        return self.name 





