from email.mime import image
from django.db import models
from applications.departamento.models import Department
from django.db.models.signals import post_save 
from .managers import EmpleadoManager
from PIL import Image

# Create your models here.


class Skills(models.Model):
    name = models.CharField('Habilidad',max_length=50)

    class Meta:
        verbose_name = 'Habilidad'
        verbose_name_plural = 'Habilidades Empleados'

    def __str__(self):
        return str(self.id) + '-' + self.name





class Empleado(models.Model):
    
    # choices
    MASCULINO = '0'
    FEMENINO = '1'
    OTRO = 3
    GENDER_CHOICES = [
        (MASCULINO, 'Masculino'),
        (FEMENINO, 'Femenino'),
        (OTRO, 'Otro'),
    ]

    
    first_name = models.CharField('Nombres',max_length=60)
    last_name = models.CharField('Apellidos',max_length=60)
    full_name = models.CharField('Nombres Completos',max_length=120, blank=True)
    gender = models.CharField('Genero',max_length=50, choices=GENDER_CHOICES)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    image = models.ImageField(max_length=2000 , upload_to='empleado',blank=True, null=True)
    skills = models.ManyToManyField(Skills)
    observations = models.TextField(blank=True , null=True)
    anulate = models.BooleanField('Anulado',default=False, null=True)
    objects = EmpleadoManager()

    def __str__(self):
        return str(self.id) + '-' + self.first_name + '-' + self.last_name


    
# #Optimizar imagen sea menos pesada
# def optimize_image(sender, instance, **kwargs):
#     print("==================")
#     if instance.image:
#         image = Image.open(instance.image.path)
#         image.save(instance.image.path, quality=20 , optimize=True)



# post_save.connect(optimize_image, sender=Empleado)