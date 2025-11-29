"""
* EJERCICIO:
 * Utilizando tu lenguaje, emplea 3 mecanismos diferentes para imprimir
 * números del 1 al 10 mediante iteración.
 *
 * DIFICULTAD EXTRA (opcional):
 * Escribe el mayor número de mecanismos que posea tu lenguaje
 * para iterar valores. ¿Eres capaz de utilizar 5? ¿Y 10?
 """

for i in range(10):
    print(i+1)

i = 1
while True:
    if i <= 10:
        print(i)
        i = i + 1
    else: break

def count(num: int):
    if num <=10:
        print(num)
        count(num + 1)
count(1)

#extra
for e in [1, 2, 3, 4]:
    print(e)

for e in {1, 2, 3, 4}:
    print(e)

for e in (1, 2, 3, 4):
    print(e)

for c in "Python":
    print(c)

for e in reversed([1, 2, 3, 4]):
    print(e)

