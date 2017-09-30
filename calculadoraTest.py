from unittest import TestCase

from Calculadora import Calculadora

class CalculadoraTest(TestCase):
    def test_suma(self):
        self.assertEquals(Calculadora().suma(""),0,"cadena vacia")

    def test_suma_unacadena(self):
        self.assertEquals(Calculadora().suma("1"),1,"Un numero")

    def test_suma_cadenaConUnnumero(self):
        self.assertEquals(Calculadora().suma("1"),1,"Un numero")
        self.assertEquals(Calculadora().suma("2"),2,"Un numero")

    def test_suma_cadenaConDosnumeros(self):
        self.assertEquals(Calculadora().suma("1,3"),4,"Dos numeros")

    def test_suma_cadenaConMultiplesnumeros(self):
        self.assertEquals(Calculadora().suma("5,2,4,1"),12,"Multiples numeros")