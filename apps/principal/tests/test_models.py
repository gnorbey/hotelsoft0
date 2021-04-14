from django.test import TestCase
from apps.principal.models import Habitacion, TipoHabitacion

class HabitacionTestCase(TestCase):
    def setUp(self):
        Habitacion.objects.create(numero="302", estado="Activo", costo=32000, descripcion= "habitacion con vista al mar", tipo="sencilla")
        Habitacion.objects.create(numero="1010", estado="Activo", costo=34000, descripcion= "habitacion con vista al mar", tipo="sencilla")
    def test_habitaciones_tienen_costo(self):
        """Las habitaciones tienen el costo temporalmente definido"""
        costo1 = Habitacion.objects.get(costo=32000)
        costo2 = Habitacion.objects.get(costo=34000)
        self.assertEqual(costo1.costo, costo2.costo, 32000)
        self.assertEqual(costo2.costo, costo1.costo, 34000)