"""
* EJERCICIO:
 * Empleando tu lenguaje, explora la definición del tipo de dato
 * que sirva para definir enumeraciones (Enum).
 * Crea un Enum que represente los días de la semana del lunes
 * al domingo, en ese orden. Con ese enumerado, crea una operación
 * que muestre el nombre del día de la semana dependiendo del número entero
 * utilizado (del 1 al 7).
 """
#nota: ya que estoy sigo probando recursividad y manejo de errores basico
from enum import Enum
def escribir_dia():
    try:
        num = int(input("ingresa un numero valido (del 1 al 7): "))
        return num
    except ValueError:
        escribir_dia()

class Dias_semana(Enum):
    Lunes = 1
    Martes = 2
    Miercoles = 3
    Jueves = 4
    Viernes = 5
    Sabado = 6
    Domingo = 7

def muestra_dia(num: int):
    if num <= 7 and num >= 0:
        print(Dias_semana(num).name)
    else:
        num = escribir_dia()
        muestra_dia(num)    
try:
    num = int(input("ingrese un numero del 1 al 7 correspondiente a un dia de la semana: "))
except ValueError:
    num = escribir_dia()
muestra_dia(num)

"""
*
 * DIFICULTAD EXTRA (opcional):
 * Crea un pequeño sistema de gestión del estado de pedidos.
 * Implementa una clase que defina un pedido con las siguientes características:
 * - El pedido tiene un identificador y un estado.
 * - El estado es un Enum con estos valores: PENDIENTE, ENVIADO, ENTREGADO y CANCELADO.
 * - Implementa las funciones que sirvan para modificar el estado:
 *   - Pedido enviado
 *   - Pedido cancelado
 *   - Pedido entregado
 *   (Establece una lógica, por ejemplo, no se puede entregar si no se ha enviado, etc...)
 * - Implementa una función para mostrar un texto descriptivo según el estado actual.
 * - Crea diferentes pedidos y muestra cómo se interactúa con ellos. 
 """

#extra
class Estado_pedido(Enum):
    Pendiente = 1
    Enviado = 2
    entregado = 3
    cancelado = 4

class pedido:
    estado = Estado_pedido.Pendiente

    def __init__(self, id) -> None:
        self.id = id
    def enviado(self):
        if self.estado == Estado_pedido.Pendiente:
            self.estado = Estado_pedido.Enviado
            self.mostrar_estado()
    def entregado(self):
        if self.estado == Estado_pedido.Enviado:
            self.estado = Estado_pedido.entregado
            self.mostrar_estado()
    def cancelado(self):
        if self.estado != Estado_pedido.entregado:
            self.estado = Estado_pedido.cancelado
            self.mostrar_estado()
        else:
            print("El pedido no se puede cancelar, ya que este fue entregado")
    def mostrar_estado(self):
        print(f"el estado del pedido {self.id} es {self.estado.name}")

pedido_1 = pedido(1)
pedido_1.mostrar_estado()
pedido_1.enviado()
pedido_1.entregado()
pedido_1.cancelado()
