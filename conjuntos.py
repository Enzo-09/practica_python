"""
* EJERCICIO:
 * Utilizando tu lenguaje crea un conjunto de datos y realiza las siguientes
 * operaciones (debes utilizar una estructura que las soporte):
 * - Añade un elemento al final.
 * - Añade un elemento al principio.
 * - Añade varios elementos en bloque al final.
 * - Añade varios elementos en bloque en una posición concreta.
 * - Elimina un elemento en una posición concreta.
 * - Actualiza el valor de un elemento en una posición concreta.
 * - Comprueba si un elemento está en un conjunto.
 * - Elimina todo el contenido del conjunto.
 *
 * DIFICULTAD EXTRA (opcional):
 * Muestra ejemplos de las siguientes operaciones con conjuntos:
 * - Unión.
 * - Intersección.
 * - Diferencia.
 * - Diferencia simétrica.
 """

una_lista = ["enzo", 19, "f1"]
una_lista.append("prueba al final")
una_lista.insert(0, "lol")
print(una_lista)
una_lista.extend(["3 elementos", "al final", "de la lista"])
una_lista[3:4] = [[1, 3, 443]]
print(una_lista)
una_lista[0] = "actualiza2"
print(f"Comprobar si un elemento existe: {-1 in una_lista}")
print(f"Eliminar el contenido: {una_lista.clear()}")

#extra
set_1 = {1, 3, 5, 7, 9}
set_2 = {2, 4, 6, 8, 9}

print(f"{set_1.union(set_2)}")
print(f"{set_1.intersection(set_2)}")
print(f"{set_1.difference(set_2)}")
print(f"{set_1.symmetric_difference(set_2)}")

