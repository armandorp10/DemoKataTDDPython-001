from unittest import TestCase

import Calculadora

class CalculadoraTest(TestCase):
    def test_suma(self):
        self.assertEquals(Calculadora().suma(""),0,"cadena vacia")
