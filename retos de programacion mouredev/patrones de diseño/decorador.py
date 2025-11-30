"""
* EJERCICIO:
 * Explora el concepto de "decorador" y muestra cómo crearlo
 * con un ejemplo genérico.
 """

def print_call(funcion):
    def print_funcion():
        print((f"la funcion {funcion.__name__} ha sido llamada"))
        return funcion
    return print_funcion
@print_call
def example_function():
    pass


@print_call
def example_function_2():
    pass


@print_call
def example_function_3():
    pass


example_function()
example_function_2()
example_function_3()

"""
 * DIFICULTAD EXTRA (opcional):
 * Crea un decorador que sea capaz de contabilizar cuántas veces
 * se ha llamado a una función y aplícalo a una función de tu elección.
 """

def contar_cantidad(function):
    def recibir_funcion():
        recibir_funcion.call_count += 1
        print(f"la funcion {function} se ha llamado {recibir_funcion.call_count} veces")
        return function

    recibir_funcion.call_count = 0
    return recibir_funcion

@contar_cantidad
def example_function_4():
    pass


@contar_cantidad
def example_function_5():
    pass


example_function_4()
example_function_4()
example_function_4()
example_function_4()
example_function_5()
example_function_4()
example_function_5()