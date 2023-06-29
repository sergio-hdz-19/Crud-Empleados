from django.contrib import admin
from .models import Empleado,Skills
# Register your models here.


admin.site.register({ 
                     Skills,
                     Empleado
                     })


class EmpleadoAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'first_name',
        'last_name',
        'departamento',
        'gender'
        'full_name',
        
    )

    def full_name(self,obj):
        return obj.first_name + ' ' + obj.last_name 


    search_fields = ('first_name',)
    list_filter = ('departamento','skills')
    filter_horizontal = ('skills',)

