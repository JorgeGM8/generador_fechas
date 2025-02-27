print('''¡Bienvenid@ al generador de fechas por Jorge G.M.!
Aquí podrás especificar un rango de fechas para sacar un listado de todas ellas, incluyendo únicamente los días de la semana que quieras.
¡Comencemos!\n''')


from datetime import date

# Creación de la fecha de inicio.

inicio = input('Introduce la fecha de inicio en formato DD/MM/AAAA: ').split('/')

dia_inicio = int(inicio[0])
mes_inicio = int(inicio[1])
agno_inicio = int(inicio[2])

inicio = date(agno_inicio,mes_inicio,dia_inicio)


# Creación de la fecha final.

final = input('Introduce la fecha final en formato DD/MM/AAAA: ').split('/')

dia_final = int(final[0])
mes_final = int(final[1])
agno_final = int(final[2])

final = date(agno_final,mes_final,dia_final)


# Elección de los días de la semana.

dias_semana = input('''Siguiendo el formato:
L - lunes, M - martes, X - miércoles, J - jueves, V - viernes, S - sábado, D - domingo
Elige los días de la semana que deseas incluir en el listado de fechas, sin separar: ''')

# Se reemplazan los días de la semana por int para usarlos más adelante con .weekday().

dias_semana = dias_semana.replace('L','0')
dias_semana = dias_semana.replace('M','1')
dias_semana = dias_semana.replace('X','2')
dias_semana = dias_semana.replace('J','3')
dias_semana = dias_semana.replace('V','4')
dias_semana = dias_semana.replace('S','5')
dias_semana = dias_semana.replace('D','6')

dias_semana = list(map(int, dias_semana))


# Print de los días seleccionados.

from datetime import timedelta

for i in range(int((final - inicio).days) + 1):
    if (inicio + timedelta(i)).weekday() in dias_semana:
        print((inicio + timedelta(i)).strftime('%d/%m/%Y'))

input('Pulsa cualquier tecla para salir del programa.')