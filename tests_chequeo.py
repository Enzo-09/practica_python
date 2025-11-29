"""
* EJERCICIO:
 * Crea una función que se encargue de sumar dos números y retornar
 * su resultado.
 * Crea un test, utilizando las herramientas de tu lenguaje, que sea
 * capaz de determinar si esa función se ejecuta correctamente.
 """

num_1 = int(input("ingrese el primer numemro a sumar: "))
num_2 = int(input("ingrese el segundo numemro a sumar: "))

def suma(num_1:int, num_2:int):
    num_final = (num_1 + num_2)
    return num_final

num_final = suma(num_1, num_2)
print(num_final)

import unittest

class testSuma(unittest.TestCase):
    def testSumaPositivos(self):
        resultado = suma(5, 3)
        self.assertEqual(resultado, 8, "deberia ser 8")
    def sumaConCero(self):
        resultado = suma(10, 0)
        self.assertEqual(resultado, 10, "el resultado deberia ser 10")
    def testSumaNegativos(self):
        resultado = suma(5, -1)
        self.assertEqual(resultado, 4, "deberia ser 4")

if __name__ == '__main__':
    unittest.main()

"""
* DIFICULTAD EXTRA (opcional):
 * Crea un diccionario con las siguientes claves y valores:
 * "name": "Tu nombre"
 * "age": "Tu edad"
 * "birth_date": "Tu fecha de nacimiento"
 * "programming_languages": ["Listado de lenguajes de programación"]
 * Crea dos test:
 * - Un primero que determine que existen todos los campos.
 * - Un segundo que determine que los datos introducidos son correctos.
"""


class TestData(unittest.TestCase):
    def setUp(self) -> None:
        self.data = { 
        "name": "Enzo",
        "age": "21",
        "birth_date": "09-08-2004",
        "programming_languajes": "[python, typescript, react]"
        }

    def text_fields_exists(self):
        self.assertIn("name", self.data)
        self.assertIn("age", self.data)
        self.assertIn("birth_date", self.data)
        self.assertIn("programming_languages", self.data)

    def test_data_is_correct(self):
        self.assertIsInstance(self.data["name", str])
        self.assertIsInstance(self.data["age"], int)
        self.assertIsInstance(self.data["birth_date"], date)
        self.assertIsInstance(self.data["programming_languages"], list)
unittest.main()