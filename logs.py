"""
* EJERCICIO:
 * Explora el concepto de "logging" en tu lenguaje. Configúralo y muestra
 * un ejemplo con cada nivel de "severidad" disponible.
 """

import logging
import time
def sumar(a, b):
    print(a + b)
    logging.info(f"se esta intentando sumar")
    logging.debug(f"el programa funciona joya")

def dividir(a, b):
    try:
        logging.warning(f"asegurese que el segundo numero no sea 0")
        print (a / b)
    except ZeroDivisionError:
        logging.error(f"esta intentando dividir por 0")
        logging.critical(f"deteniendo el programa") 

num = int(input("ingrese el numerador: "))
numero = int(input("ingrese el denominador: "))
sumar(num, numero)
dividir(num, numero)


"""
 * DIFICULTAD EXTRA (opcional):
 * Crea un programa ficticio de gestión de tareas que permita añadir, eliminar
 * y listar dichas tareas.
 * - Añadir: recibe nombre y descripción.
 * - Eliminar: por nombre de la tarea.
 * Implementa diferentes mensajes de log que muestren información según la
 * tarea ejecutada (a tu elección).
 * Utiliza el log para visualizar el tiempo de ejecución de cada tarea.
 """

class tareas:
    def __init__(self) -> None:
        self.tasks = {}
    
    def add_task(self, nombre, descripcion):
        start_time = time.time()
        if nombre not in self.tasks:
            self.tasks[nombre] = descripcion
            logging.info(f"tarea {nombre} agregada")
        else:
            logging.error(f"la tarea ya se encuentra en la lista")
        logging.debug(f"numero de tareas: {len(self.tasks)}")
        end_time = time.time()
        self._print_time(start_time, end_time)
    
    def del_task(self, nombre):
        start_time = time.time()
        if nombre in self.tasks:
            del self.tasks[nombre]
            logging.info(f"se ha eliminado la tarea {nombre}")
        else:
            logging.error("la tarea no existe.")
        logging.debug(f"numero de tareas: {len(self.tasks)}")
        end_time = time.time()
        self._print_time(start_time, end_time)
    
    def list_tasks(self):
        start_time = time.time()
        if self.tasks:
            logging.info("se van a imprimir las tareas:")
            for nombre, descripcion in self.tasks.items():
                print(f"{nombre}, {descripcion}.")
        else:
            logging.critical("no hay tareas para mostrar")
        end_time = time.time()
        self._print_time(start_time, end_time)
    def _print_time(self, start_time, end_time):
        logging.debug(f"tiempo de ejecucion: {end_time - start_time:.6f} segundos")


task_manager = tareas()
task_manager.list_tasks()
task_manager.add_task("Pan", "Comprar 5 barras de pan")
task_manager.add_task("Python", "Estudiar Python")
task_manager.list_tasks()
task_manager.del_task("Python")
task_manager.list_tasks()
task_manager.add_task("Pan", "Comprar 5 barras de pan")
task_manager.del_task("Python")