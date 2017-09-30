from unittest import TestCase

from Calculadora import Calculadora

class CalculadoraTest(TestCase):
    def test_suma(self):
        self.assertEquals(Calculadora().suma(""),0,"cadena vacia")

    def test_suma_unacadena(self):
        self.assertEquals(Calculadora().suma("1"),1,"Un numero")

    def test_suma_unacadena(self):
        self.assertEquals(Calculadora().suma("1"),1,"Un numero")
        self.assertEquals(Calculadora().suma("2"),2,"Un numero")