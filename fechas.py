"""
* EJERCICIO:
 * Crea dos variables utilizando los objetos fecha (date, o semejante) de tu lenguaje:
 * - Una primera que represente la fecha (día, mes, año, hora, minuto, segundo) actual.
 * - Una segunda que represente tu fecha de nacimiento (te puedes inventar la hora).
 * Calcula cuántos años han transcurrido entre ambas fechas.
 """
from datetime import datetime
date_today = datetime.today()
print(date_today)
date_birth = datetime(2004, 8, 9, 12, 30, 45)
print(date_birth)

diferencia = date_today - date_birth
print(diferencia.days // 365)

""" 
* DIFICULTAD EXTRA (opcional):
 * Utilizando la fecha de tu cumpleaños, formatéala y muestra su resultado de
 * 10 maneras diferentes. Por ejemplo:
 * - Día, mes y año.
 * - Hora, minuto y segundo.
 * - Día de año.
 * - Día de la semana.
 * - Nombre del mes.
 * (lo que se te ocurra...)
 """


print(date_birth.strftime("%d/%m/%y"))
print(date_birth.strftime("%d/%m/%Y"))
print(date_birth.strftime("%H:%M:%S"))
print(date_birth.strftime("%j"))
print(date_birth.strftime("%A"))
print(date_birth.strftime("%h"))
print(date_birth.strftime("%B"))
print(date_birth.strftime("%c"))
print(date_birth.strftime("%x"))
print(date_birth.strftime("%X"))
print(date_birth.strftime("%p"))