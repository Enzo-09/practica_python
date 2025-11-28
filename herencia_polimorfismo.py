"""
* EJERCICIO:
 * Explora el concepto de herencia según tu lenguaje. Crea un ejemplo que
 * implemente una superclase Animal y un par de subclases Perro y Gato,
 * junto con una función que sirva para imprimir el sonido que emite cada Animal.
 *
 """

class animal:
    def __init__(self, name:str):
        self.name = name
    
    def sound(self):
        pass

class perro(animal):
    def sound(self):
        print("guau")
class gato(animal):
    def sound(self):
        print("Miau")
def print_sound(animal: animal):
    animal.sound()

animal_prueba = animal("animal")
print_sound(animal_prueba)
washinton = perro("Perro")
print_sound(washinton)
leo = gato("Gato")
print_sound(leo)

"""
 * DIFICULTAD EXTRA (opcional):
 * Implementa la jerarquía de una empresa de desarrollo formada por Empleados que
 * pueden ser Gerentes, Gerentes de Proyectos o Programadores.
 * Cada empleado tiene un identificador y un nombre.
 * Dependiendo de su labor, tienen propiedades y funciones exclusivas de su
 * actividad, y almacenan los empleados a su cargo.
 """

class empleados:
    def __init__(self,identificador: int, nombre:str):
        self.id = identificador
        self.nombre = nombre
        self.empleado = []
    
    def add(self, empleados):
        self.empleado.append(empleados)
    
    def print_empleados(self):
        print(f"Lista de empleados a cargo de {self.nombre}:")
        for empleado in self.empleado:
            print(f"{empleado.nombre}")

class gerentes(empleados):
    def coordina_proyectos(self):
        print(f"{self.nombre} esta coordinando los proyectos")
        
class gerente_proyecto(empleados):
    def __init__(self, identificador: int, nombre:str, proyecto_asignado: str):
        super().__init__(identificador, nombre)
        self.proyecto_asignado = proyecto_asignado
    
    def coordina_unico_proyecto(self):
        print(f"{self.nombre} esta coordinando su proyecto")    

class programador(empleados):
    def __init__(self, identificador, nombre, lenguaje, proyecto):
        super().__init__(identificador, nombre)
        self.lenguaje = lenguaje
        self.proyecto = proyecto

    def programa(self):
        print(f"{self.nombre} esta programando")



programador_1 = programador(1, "Lionel", "TypeScript", "App Móvil")
gerente_1 = gerente_proyecto(2, "Juan", "ERP Financiero")
jefe_superior = empleados(99, "Enzo")
jefe_superior.add(programador_1)
jefe_superior.add(gerente_1)
programador_1.programa()
gerente_1.coordina_unico_proyecto()
jefe_superior.print_empleados()