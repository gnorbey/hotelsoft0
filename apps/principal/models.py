from django.db import models



# Create your models here.
class Nacionalidad (models.Model):
    id = models.AutoField(primary_key = True)
    pais = models.CharField(max_length=50)
    nacionalidad = models.CharField( max_length=70)




class TipoHabitacion (models.Model):
    id = models.AutoField(blank = False ,primary_key = True)
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField(max_length = 100)

    def __str__(self):
        return '{}'.format(self.nombre)

  

class Estado (models.Model):
    id = models.AutoField(blank = False ,primary_key = True)
    nombre = models.CharField(null= False ,blank = False, max_length = 50)

    def __str__(self):
        return '{}'.format(self.nombre)
    
    

class Habitacion (models.Model):
    id = models.AutoField(blank = False ,primary_key = True)
    numero = models.CharField(null= False ,blank = False ,max_length=5)
    estado = models.ForeignKey(Estado , on_delete = models.CASCADE)
    costo = models.IntegerField(null= False , blank = False)
    descripcion = models.TextField(max_length = 100)
    tipo = models.ForeignKey(TipoHabitacion , on_delete=models.CASCADE)

    def __str__(self):
        return '{} {}'.format(self.estado, self.tipo)   

class Cliente (models.Model):
    id = models.AutoField(blank = False ,primary_key = True)
    nombre = models.CharField(blank = False, max_length= 60)
    direcion = models.CharField(max_length=50)
    documento = models.CharField (max_length = 30)
    telefono = models.CharField( max_length=50)
    nacionalidad =models.ForeignKey(Nacionalidad, null = False, blank =False, on_delete=models.CASCADE)



class Registrador (models.Model):
    id = models.AutoField(blank = False ,primary_key = True)
    nombre =  models.CharField (blank = False, max_length= 60)
    direcion = models.CharField (max_length=50)
    documento = models.CharField (max_length = 30)
    estado = models.ForeignKey (Estado, null = False, blank =False, on_delete= models.CASCADE)
    telefono = models.CharField( max_length=50)
    observacion = models.TextField (max_length = 100)



class Alquiler (models.Model):
    fechaHoraEntrada = models.DateTimeField(null = False ,blank = False , auto_now=False, auto_now_add=False)
    fechaHoraSalida = models.DateTimeField(null = False ,blank = False , auto_now=False, auto_now_add=False)
    costoTotal = models.IntegerField()
    observacion = models.TextField(max_length = 100)
    habitacion = models.ForeignKey(Habitacion, on_delete=models.CASCADE)
    cliente =  models.ForeignKey(Cliente, on_delete=models.CASCADE)
    registrador = models.ForeignKey(Registrador, on_delete=models.CASCADE)
    estado = models.ForeignKey(Estado,on_delete=models.CASCADE)


