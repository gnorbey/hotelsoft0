from django.contrib import admin

from apps.principal.models import Alquiler, Cliente, Estado, Habitacion, Nacionalidad, Registrador, TipoHabitacion

# Register your models here.
admin.site.register(Alquiler)
admin.site.register(Cliente)
admin.site.register(Estado)
admin.site.register(Habitacion)
admin.site.register(Nacionalidad)
admin.site.register(Registrador)
admin.site.register(TipoHabitacion)