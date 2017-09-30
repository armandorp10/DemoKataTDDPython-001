from unittest import TestCase

from Calculadora import Calculadora

class CalculadoraTest(TestCase):
    def test_suma(self):
        self.assertEquals(Calculadora().suma(""),0,"cadena vacia")
